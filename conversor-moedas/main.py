from converter import CurrencyConverter, ConversorError
from api_handler import APIHandler
import os


def clear_screen():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text):
    """Imprime um cabeçalho formatado"""
    print("\n" + "="*70)
    print(text.center(70))
    print("="*70)


def print_section(text):
    """Imprime um separador de seção"""
    print("\n" + "-"*70)
    print(text)
    print("-"*70)


def menu_principal():
    """Menu principal do conversor"""
    converter = CurrencyConverter()

    while True:
        clear_screen()
        print_header("CONVERSOR DE MOEDAS")

        print("\n1. Converter moeda")
        print("2. Ver taxa de câmbio")
        print("3. Tabela de câmbio completa")
        print("4. Converter para múltiplas moedas")
        print("5. Atualizar taxas via API")
        print("6. Informações de moeda")
        print("7. Sair")

        print("="*70)
        opcao = input("Escolha uma opção (1-7): ").strip()

        if opcao == "1":
            converter_simples(converter)
        elif opcao == "2":
            ver_taxa_cambio(converter)
        elif opcao == "3":
            tabela_cambio(converter)
        elif opcao == "4":
            converter_multiplo(converter)
        elif opcao == "5":
            atualizar_api(converter)
        elif opcao == "6":
            info_moeda(converter)
        elif opcao == "7":
            print("\n👋 Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
            input("Pressione ENTER para continuar...")


def converter_simples(converter: CurrencyConverter):
    """Converte um valor entre duas moedas"""
    print_header("CONVERTER MOEDA")

    try:
        print("\nMoedas disponíveis:")
        moedas = converter.get_supported_currencies()
        for i, moeda in enumerate(moedas, 1):
            info = converter.get_currency_info(moeda)
            print(f"  {i:2d}. {info['code']:<5} - {info['name']}")

        origem = input("\nDigite a moeda origem (ex: BRL): ").strip().upper()
        if origem not in moedas:
            print("❌ Moeda origem inválida!")
            return

        destino = input("Digite a moeda destino (ex: USD): ").strip().upper()
        if destino not in moedas:
            print("❌ Moeda destino inválida!")
            return

        valor = float(input("Digite o valor: "))

        resultado = converter.convert(valor, origem, destino)
        print_section("RESULTADO DA CONVERSÃO")
        print(f"\n{converter.format_currency(valor, origem)} = {converter.format_currency(resultado, destino)}")
        print(f"\nTaxa de conversão: 1 {origem} = {converter.convert(1, origem, destino):.4f} {destino}")

        input("\nPressione ENTER para continuar...")

    except ValueError:
        print("❌ Valor inválido! Digite um número.")
    except ConversorError as e:
        print(f"❌ Erro: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

    input("Pressione ENTER para continuar...")


def ver_taxa_cambio(converter: CurrencyConverter):
    """Exibe taxa de câmbio de uma moeda específica"""
    print_header("TAXA DE CÂMBIO")

    try:
        moedas = converter.get_supported_currencies()
        print("\nMoedas disponíveis:")
        for i, moeda in enumerate(moedas, 1):
            info = converter.get_currency_info(moeda)
            print(f"  {i:2d}. {info['code']:<5} - {info['name']}")

        moeda = input("\nDigite a moeda (ex: BRL): ").strip().upper()
        info = converter.get_currency_info(moeda)

        print_section(f"INFORMAÇÕES - {info['name']}")
        print(f"\nCódigo: {info['code']}")
        print(f"Símbolo: {info['symbol']}")
        print(f"Taxa para USD: {info['rate_to_usd']:.4f}")
        print(f"Significado: 1 USD = {info['rate_to_usd']:.4f} {info['code']}")

    except ConversorError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER para continuar...")


def tabela_cambio(converter: CurrencyConverter):
    """Exibe tabela completa de câmbio"""
    print_header("TABELA DE CÂMBIO")

    try:
        base = input("Digite a moeda base (USD/BRL/EUR): ").strip().upper() or 'USD'
        print(converter.get_exchange_table(base))

    except ConversorError as e:
        print(f"❌ Erro: {e}")

    input("Pressione ENTER para continuar...")


def converter_multiplo(converter: CurrencyConverter):
    """Converte um valor para múltiplas moedas"""
    print_header("CONVERTER PARA MÚLTIPLAS MOEDAS")

    try:
        moedas = converter.get_supported_currencies()
        print("\nMoedas disponíveis:")
        for i, moeda in enumerate(moedas, 1):
            info = converter.get_currency_info(moeda)
            print(f"  {i:2d}. {info['code']:<5} - {info['name']}")

        origem = input("\nDigite a moeda origem (ex: BRL): ").strip().upper()
        if origem not in moedas:
            print("❌ Moeda origem inválida!")
            return

        valor = float(input("Digite o valor: "))

        conversoes = converter.get_conversion_summary(valor, origem)

        print_section(f"CONVERSÕES DE {converter.format_currency(valor, origem)}")
        print()

        for moeda in sorted(conversoes.keys()):
            valor_convertido = conversoes[moeda]
            info = converter.get_currency_info(moeda)
            print(f"{info['code']:5} - {converter.format_currency(valor_convertido, moeda):>20}")

    except ValueError:
        print("❌ Valor inválido!")
    except ConversorError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER para continuar...")


def atualizar_api(converter: CurrencyConverter):
    """Atualiza taxas via API"""
    print_header("ATUALIZAR TAXAS VIA API")

    try:
        api_handler = APIHandler()
        print("\n⏳ Conectando à API de câmbio...")
        data = api_handler.update_with_cache_fallback()

        if data:
            for moeda, taxa in data['rates'].items():
                if moeda in converter.rates:
                    converter.update_rate(moeda, taxa)

            print("\n✅ Taxas atualizadas com sucesso!")
            print(f"Base: {data['base']}")
            print(f"Moedas atualizadas: {len(data['rates'])}")
        else:
            print("\n❌ Não foi possível atualizar as taxas.")

    except Exception as e:
        print(f"❌ Erro ao atualizar: {e}")

    input("\nPressione ENTER para continuar...")


def info_moeda(converter: CurrencyConverter):
    """Exibe informações detalhadas de uma moeda"""
    print_header("INFORMAÇÕES DE MOEDA")

    try:
        moedas = converter.get_supported_currencies()
        print("\nMoedas disponíveis:")
        for i, moeda in enumerate(moedas, 1):
            info = converter.get_currency_info(moeda)
            print(f"  {i:2d}. {info['code']:<5} - {info['name']}")

        moeda = input("\nDigite a moeda (ex: BRL): ").strip().upper()
        info = converter.get_currency_info(moeda)

        print_section(f"INFORMAÇÕES DETALHADAS - {info['name']}")
        print(f"\n📌 Código ISO:        {info['code']}")
        print(f"📛 Nome:              {info['name']}")
        print(f"💱 Símbolo:           {info['symbol']}")
        print(f"📊 Taxa para 1 USD:   {info['rate_to_usd']:.4f} {info['code']}")
        print(f"\nExemplos de conversão:")

        exemplos = [100, 500, 1000]
        for exemplo in exemplos:
            em_usd = converter.convert(exemplo, moeda, 'USD')
            print(f"  {converter.format_currency(exemplo, moeda):>15} = {converter.format_currency(em_usd, 'USD')}")

    except ConversorError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrompido pelo usuário.")
