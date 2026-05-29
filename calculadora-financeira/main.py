import os
import sys
from juros import InterestCalculator, FinanceError
from investimentos import InvestmentAnalyzer
from emprestimos import LoanCalculator
from analise import FinancialAnalysis
from utils import (
    format_currency, format_percent, format_number,
    annual_to_monthly_rate, monthly_to_annual_rate,
    parse_percent, summary_table, print_amortization_schedule
)


def clear_screen():
    """Limpa a tela"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text):
    """Imprime cabeçalho"""
    print("\n" + "="*70)
    print(text.center(70))
    print("="*70)


def print_section(text):
    """Imprime separador de seção"""
    print("\n" + "-"*70)
    print(text)
    print("-"*70)


def menu_principal():
    """Menu principal"""
    while True:
        clear_screen()
        print_header("CALCULADORA FINANCEIRA")
        print("\n1. Cálculos de Juros")
        print("2. Análise de Investimentos")
        print("3. Empréstimos e Financiamentos")
        print("4. Análise Financeira Geral")
        print("5. Conversão de Taxas")
        print("6. Sair")
        print("="*70)

        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            menu_juros()
        elif opcao == "2":
            menu_investimentos()
        elif opcao == "3":
            menu_emprestimos()
        elif opcao == "4":
            menu_analise()
        elif opcao == "5":
            menu_conversao_taxas()
        elif opcao == "6":
            print("\n👋 Até logo!")
            break
        else:
            print("❌ Opção inválida!")
            input("Pressione ENTER...")


def menu_juros():
    """Menu de cálculos de juros"""
    while True:
        print_header("CÁLCULOS DE JUROS")
        print("\n1. Juros Simples")
        print("2. Juros Compostos")
        print("3. Juros Compostos Contínuos")
        print("4. Série de Depósitos")
        print("5. Voltar")
        print("="*70)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            juros_simples()
        elif opcao == "2":
            juros_compostos()
        elif opcao == "3":
            juros_continuo()
        elif opcao == "4":
            serie_depositos()
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida!")


def juros_simples():
    """Calcula juros simples"""
    try:
        print_header("JUROS SIMPLES")
        principal = float(input("Capital inicial (R$): "))
        taxa = float(input("Taxa de juros (ex: 5 para 5%): ")) / 100
        tempo = float(input("Período (anos): "))

        resultado = InterestCalculator.simple_interest(principal, taxa, tempo)

        print_section("RESULTADO")
        print(f"Capital: {format_currency(resultado['principal'])}")
        print(f"Taxa: {format_percent(resultado['rate'])}")
        print(f"Período: {resultado['time']} anos")
        print(f"Juros: {format_currency(resultado['interest'])}")
        print(f"Montante: {format_currency(resultado['amount'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def juros_compostos():
    """Calcula juros compostos"""
    try:
        print_header("JUROS COMPOSTOS")
        principal = float(input("Capital inicial (R$): "))
        taxa = float(input("Taxa de juros (ex: 5 para 5%): ")) / 100
        tempo = float(input("Período (anos): "))

        print("\nFrequência de capitalização:")
        print("1. Anual (1x/ano)")
        print("2. Semestral (2x/ano)")
        print("3. Trimestral (4x/ano)")
        print("4. Mensal (12x/ano)")
        print("5. Diário (365x/ano)")

        freq_opcao = input("Escolha: ").strip()
        frequencias = {"1": 1, "2": 2, "3": 4, "4": 12, "5": 365}
        frequencia = frequencias.get(freq_opcao, 12)

        resultado = InterestCalculator.compound_interest(
            principal, taxa, tempo, frequencia)

        print_section("RESULTADO")
        print(f"Capital: {format_currency(resultado['principal'])}")
        print(f"Taxa: {format_percent(resultado['rate'])}")
        print(f"Período: {resultado['time']} anos")
        print(f"Capitalização: {frequencia}x por ano")
        print(f"Juros: {format_currency(resultado['interest'])}")
        print(f"Montante: {format_currency(resultado['amount'])}")

    except (ValueError, KeyError):
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def juros_continuo():
    """Calcula juros compostos contínuos"""
    try:
        print_header("JUROS COMPOSTOS CONTÍNUOS")
        principal = float(input("Capital inicial (R$): "))
        taxa = float(input("Taxa de juros (ex: 5 para 5%): ")) / 100
        tempo = float(input("Período (anos): "))

        resultado = InterestCalculator.continuous_compound(
            principal, taxa, tempo)

        print_section("RESULTADO")
        print(f"Capital: {format_currency(resultado['principal'])}")
        print(f"Taxa: {format_percent(resultado['rate'])}")
        print(f"Período: {resultado['time']} anos")
        print(f"Juros: {format_currency(resultado['interest'])}")
        print(f"Montante: {format_currency(resultado['amount'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def serie_depositos():
    """Calcula série de depósitos"""
    try:
        print_header("SÉRIE DE DEPÓSITOS IGUAIS")
        deposito = float(input("Valor do depósito mensal (R$): "))
        taxa_anual = float(input("Taxa anual (ex: 5): ")) / 100
        taxa_mensal = annual_to_monthly_rate(taxa_anual)
        meses = int(input("Período (meses): "))

        resultado = InterestCalculator.final_amount_series(
            deposito, taxa_mensal, meses)

        print_section("RESULTADO")
        print(f"Depósito mensal: {format_currency(resultado['monthly_deposit'])}")
        print(f"Taxa mensal: {format_percent(resultado['rate'])}")
        print(f"Período: {resultado['months']} meses")
        print(f"Total depositado: {format_currency(resultado['total_deposited'])}")
        print(f"Juros acumulados: {format_currency(resultado['total_interest'])}")
        print(f"Valor final: {format_currency(resultado['final_amount'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def menu_investimentos():
    """Menu de investimentos"""
    while True:
        print_header("ANÁLISE DE INVESTIMENTOS")
        print("\n1. Calcular VPL (Valor Presente Líquido)")
        print("2. Calcular TIR (Taxa Interna de Retorno)")
        print("3. Calcular ROI (Retorno sobre Investimento)")
        print("4. Payback Simples")
        print("5. Payback Descontado")
        print("6. Comparar Projetos")
        print("7. Ponto de Equilíbrio")
        print("8. Voltar")
        print("="*70)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            calcular_vpl()
        elif opcao == "2":
            calcular_tir()
        elif opcao == "3":
            calcular_roi()
        elif opcao == "4":
            payback_simples()
        elif opcao == "5":
            payback_descontado()
        elif opcao == "6":
            comparar_projetos()
        elif opcao == "7":
            ponto_equilibrio()
        elif opcao == "8":
            break
        else:
            print("❌ Opção inválida!")


def calcular_vpl():
    """Calcula VPL"""
    try:
        print_header("VALOR PRESENTE LÍQUIDO (VPL)")
        taxa = float(input("Taxa de desconto (ex: 10): ")) / 100

        print("\nDigite os fluxos de caixa:")
        print("Primeiro deve ser negativo (investimento inicial)")

        fluxos = []
        while True:
            valor = input(f"Fluxo {len(fluxos)} (leave em branco para terminar): ").strip()
            if not valor:
                break
            fluxos.append(float(valor))

        if len(fluxos) < 2:
            print("❌ Precisa de pelo menos 2 fluxos!")
            input("Pressione ENTER...")
            return

        vpl = InvestmentAnalyzer.npv(fluxos, taxa)

        print_section("RESULTADO")
        print(f"VPL: {format_currency(vpl)}")
        print(f"Decisão: {'✅ Viável' if vpl > 0 else '❌ Não viável'}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def calcular_tir():
    """Calcula TIR"""
    try:
        print_header("TAXA INTERNA DE RETORNO (TIR)")

        print("Digite os fluxos de caixa:")
        fluxos = []
        while True:
            valor = input(f"Fluxo {len(fluxos)} (leave em branco para terminar): ").strip()
            if not valor:
                break
            fluxos.append(float(valor))

        if len(fluxos) < 2:
            print("❌ Precisa de pelo menos 2 fluxos!")
            input("Pressione ENTER...")
            return

        tir = InvestmentAnalyzer.irr(fluxos)

        print_section("RESULTADO")
        print(f"TIR: {format_percent(tir)}")
        print(f"TIR anualizada: {format_percent(tir)} a.a.")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def calcular_roi():
    """Calcula ROI"""
    try:
        print_header("RETORNO SOBRE INVESTIMENTO (ROI)")
        investimento = float(input("Investimento inicial (R$): "))
        valor_final = float(input("Valor final (R$): "))
        anos = int(input("Período (anos): "))

        resultado = InvestmentAnalyzer.roi(investimento, valor_final, anos)

        print_section("RESULTADO")
        print(f"ROI Total: {format_percent(resultado['roi_total_percent']/100)}")
        print(f"ROI Anual: {format_percent(resultado['roi_annual_percent']/100)}")
        print(f"Ganho: {format_currency(resultado['gain'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def payback_simples():
    """Calcula Payback Simples"""
    try:
        print_header("PAYBACK SIMPLES")

        print("Digite os fluxos de caixa:")
        fluxos = []
        while True:
            valor = input(f"Fluxo {len(fluxos)} (leave em branco para terminar): ").strip()
            if not valor:
                break
            fluxos.append(float(valor))

        resultado = InvestmentAnalyzer.payback_simple(fluxos)

        print_section("RESULTADO")
        if resultado['has_payback']:
            print(f"Payback: {resultado['payback_period']:.2f} anos")
            print("✅ Investimento recuperado!")
        else:
            print("❌ Investimento nunca é recuperado")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def payback_descontado():
    """Calcula Payback Descontado"""
    try:
        print_header("PAYBACK DESCONTADO")
        taxa = float(input("Taxa de desconto (ex: 10): ")) / 100

        print("Digite os fluxos de caixa:")
        fluxos = []
        while True:
            valor = input(f"Fluxo {len(fluxos)} (leave em branco para terminar): ").strip()
            if not valor:
                break
            fluxos.append(float(valor))

        resultado = InvestmentAnalyzer.payback_discounted(fluxos, taxa)

        print_section("RESULTADO")
        if resultado['has_payback']:
            print(f"Payback: {resultado['payback_period']:.2f} anos")
            print("✅ Investimento recuperado!")
        else:
            print("❌ Investimento nunca é recuperado")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def comparar_projetos():
    """Compara múltiplos projetos"""
    try:
        print_header("COMPARAÇÃO DE PROJETOS")
        taxa = float(input("Taxa de desconto (ex: 10): ")) / 100
        num_projetos = int(input("Número de projetos: "))

        projetos = {}
        for i in range(num_projetos):
            nome = input(f"\nNome do projeto {i+1}: ")
            print(f"Fluxos de caixa do {nome}:")
            fluxos = []
            while True:
                valor = input(f"  Fluxo {len(fluxos)} (leave em branco para terminar): ").strip()
                if not valor:
                    break
                fluxos.append(float(valor))
            projetos[nome] = fluxos

        resultado = InvestmentAnalyzer.comparison_npv_irr(projetos, taxa)

        print_section("RESULTADO DA COMPARAÇÃO")
        for nome, dados in resultado.items():
            if 'error' in dados:
                print(f"{nome}: ❌ {dados['error']}")
            else:
                print(f"\n{nome}:")
                print(f"  VPL: {format_currency(dados['npv'])}")
                print(f"  TIR: {format_percent(dados['irr'])}")
                print(f"  Índice de Rentabilidade: {dados['profitability_index']:.2f}")
                print(f"  Recomendado: {'✅ Sim' if dados['recommended'] else '❌ Não'}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def ponto_equilibrio():
    """Calcula ponto de equilíbrio"""
    try:
        print_header("PONTO DE EQUILÍBRIO (BREAK EVEN)")
        custos_fixos = float(input("Custos fixos mensais (R$): "))
        custo_unitario = float(input("Custo variável por unidade (R$): "))
        preco_venda = float(input("Preço de venda por unidade (R$): "))

        resultado = InvestmentAnalyzer.break_even_analysis(
            custos_fixos, custo_unitario, preco_venda)

        print_section("RESULTADO")
        print(f"Quantidade no ponto de equilíbrio: {resultado['break_even_quantity']:.0f} unidades")
        print(f"Receita no ponto de equilíbrio: {format_currency(resultado['break_even_revenue'])}")
        print(f"Margem de contribuição: {format_currency(resultado['contribution_margin'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def menu_emprestimos():
    """Menu de empréstimos"""
    while True:
        print_header("EMPRÉSTIMOS E FINANCIAMENTOS")
        print("\n1. Sistema PRICE (Prestações Iguais)")
        print("2. Sistema SAC (Amortização Constante)")
        print("3. Comparar PRICE vs SAC")
        print("4. Refinanciamento")
        print("5. Voltar")
        print("="*70)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            calcular_price()
        elif opcao == "2":
            calcular_sac()
        elif opcao == "3":
            comparar_sistemas()
        elif opcao == "4":
            refinanciamento()
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida!")


def calcular_price():
    """Calcula Sistema PRICE"""
    try:
        print_header("SISTEMA PRICE (PRESTAÇÕES IGUAIS)")
        valor = float(input("Valor do empréstimo (R$): "))
        taxa_anual = float(input("Taxa anual (ex: 12): ")) / 100
        taxa_mensal = annual_to_monthly_rate(taxa_anual)
        meses = int(input("Período (meses): "))

        resultado = LoanCalculator.price_amortization(
            valor, taxa_mensal, meses)

        print_section("RESUMO")
        print(f"Valor: {format_currency(resultado['principal'])}")
        print(f"Taxa mensal: {format_percent(taxa_mensal)}")
        print(f"Período: {resultado['months']} meses")
        print(f"Parcela: {format_currency(resultado['monthly_payment'])}")
        print(f"Total pago: {format_currency(resultado['total_paid'])}")
        print(f"Total de juros: {format_currency(resultado['total_interest'])}")

        mostrar_tabela = input("\nDeseja ver a tabela de amortização? (s/n): ").lower()
        if mostrar_tabela == 's':
            print(print_amortization_schedule(resultado['schedule']))

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def calcular_sac():
    """Calcula Sistema SAC"""
    try:
        print_header("SISTEMA SAC (AMORTIZAÇÃO CONSTANTE)")
        valor = float(input("Valor do empréstimo (R$): "))
        taxa_anual = float(input("Taxa anual (ex: 12): ")) / 100
        taxa_mensal = annual_to_monthly_rate(taxa_anual)
        meses = int(input("Período (meses): "))

        resultado = LoanCalculator.sac_amortization(
            valor, taxa_mensal, meses)

        print_section("RESUMO")
        print(f"Valor: {format_currency(resultado['principal'])}")
        print(f"Amortização mensal: {format_currency(resultado['constant_amortization'])}")
        print(f"1ª Parcela: {format_currency(resultado['first_payment'])}")
        print(f"Última Parcela: {format_currency(resultado['last_payment'])}")
        print(f"Total pago: {format_currency(resultado['total_paid'])}")
        print(f"Total de juros: {format_currency(resultado['total_interest'])}")

        mostrar_tabela = input("\nDeseja ver a tabela de amortização? (s/n): ").lower()
        if mostrar_tabela == 's':
            print(print_amortization_schedule(resultado['schedule']))

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def comparar_sistemas():
    """Compara PRICE vs SAC"""
    try:
        print_header("COMPARAÇÃO PRICE vs SAC")
        valor = float(input("Valor do empréstimo (R$): "))
        taxa_anual = float(input("Taxa anual (ex: 12): ")) / 100
        taxa_mensal = annual_to_monthly_rate(taxa_anual)
        meses = int(input("Período (meses): "))

        resultado = LoanCalculator.compare_systems(valor, taxa_mensal, meses)

        print_section("COMPARAÇÃO")
        print("\nSISTEMA PRICE:")
        print(f"  1ª Parcela: {format_currency(resultado['price']['monthly_payment_first'])}")
        print(f"  Total pago: {format_currency(resultado['price']['total_paid'])}")
        print(f"  Total juros: {format_currency(resultado['price']['total_interest'])}")

        print("\nSISTEMA SAC:")
        print(f"  1ª Parcela: {format_currency(resultado['sac']['monthly_payment_first'])}")
        print(f"  Última Parcela: {format_currency(resultado['sac']['monthly_payment_last'])}")
        print(f"  Total pago: {format_currency(resultado['sac']['total_paid'])}")
        print(f"  Total juros: {format_currency(resultado['sac']['total_interest'])}")

        print(f"\n⭐ Sistema mais barato: {resultado['difference']['cheaper_system']}")
        print(f"Economia: {format_currency(resultado['difference']['interest_difference'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def refinanciamento():
    """Analisa refinanciamento"""
    try:
        print_header("ANÁLISE DE REFINANCIAMENTO")
        saldo = float(input("Saldo devedor atual (R$): "))
        meses_restantes = int(input("Meses ainda a pagar: "))
        taxa_atual = float(input("Taxa atual (ex: 12): ")) / 100
        taxa_nova = float(input("Taxa nova (ex: 10): ")) / 100

        taxa_atual_mensal = annual_to_monthly_rate(taxa_atual)
        taxa_nova_mensal = annual_to_monthly_rate(taxa_nova)

        resultado = LoanCalculator.refinancing_analysis(
            saldo, meses_restantes, taxa_atual_mensal, taxa_nova_mensal)

        print_section("ANÁLISE")
        print(f"Taxa atual: {format_percent(taxa_atual)}")
        print(f"Taxa nova: {format_percent(taxa_nova)}")
        print(f"Diferença: {format_percent(resultado['rate_difference'])}")
        print(f"\nJuros com taxa atual: {format_currency(resultado['current_total_interest'])}")
        print(f"Juros com taxa nova: {format_currency(resultado['new_total_interest'])}")
        print(f"Economia: {format_currency(resultado['total_savings'])}")
        print(f"Percentual: {format_percent(resultado['percentage_savings']/100)}")
        print(f"\n{'✅ Vale a pena refinanciar!' if resultado['worth_refinancing'] else '❌ Não vale a pena'}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def menu_analise():
    """Menu de análise geral"""
    while True:
        print_header("ANÁLISE FINANCEIRA GERAL")
        print("\n1. Rentabilidade Real (desconto inflação)")
        print("2. Valor Futuro com Inflação")
        print("3. WACC (Custo Médio Ponderado de Capital)")
        print("4. Análise de Endividamento")
        print("5. Análise de Portfólio")
        print("6. Voltar")
        print("="*70)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            rentabilidade_real()
        elif opcao == "2":
            valor_futuro_inflacao()
        elif opcao == "3":
            calcular_wacc()
        elif opcao == "4":
            analise_endividamento()
        elif opcao == "5":
            analise_portfolio()
        elif opcao == "6":
            break
        else:
            print("❌ Opção inválida!")


def rentabilidade_real():
    """Calcula rentabilidade real"""
    try:
        print_header("RENTABILIDADE REAL")
        rentabilidade = float(input("Rentabilidade nominal (ex: 8): ")) / 100
        inflacao = float(input("Taxa de inflação (ex: 3): ")) / 100

        resultado = FinancialAnalysis.real_return(rentabilidade, inflacao)

        print_section("RESULTADO")
        print(f"Rentabilidade nominal: {format_percent(resultado['nominal_return'])}")
        print(f"Inflação: {format_percent(resultado['inflation_rate'])}")
        print(f"Rentabilidade real: {format_percent(resultado['real_return'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def valor_futuro_inflacao():
    """Calcula valor futuro com inflação"""
    try:
        print_header("VALOR FUTURO COM INFLAÇÃO")
        valor = float(input("Valor presente (R$): "))
        inflacao = float(input("Inflação anual (ex: 5): ")) / 100
        anos = int(input("Período (anos): "))

        resultado = FinancialAnalysis.future_value_with_inflation(
            valor, inflacao, anos)

        print_section("RESULTADO")
        print(f"Valor presente: {format_currency(resultado['present_value'])}")
        print(f"Inflação anual: {format_percent(resultado['inflation_rate'])}")
        print(f"Período: {resultado['years']} anos")
        print(f"Valor futuro nominal: {format_currency(resultado['future_nominal_value'])}")
        print(f"Perda de poder de compra: {format_currency(resultado['loss_of_purchasing_power'])}")
        print(f"Percentual perdido: {format_percent(resultado['loss_percentage']/100)}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def calcular_wacc():
    """Calcula WACC"""
    try:
        print_header("WACC (Weighted Average Cost of Capital)")
        valor_patrimonio = float(input("Valor patrimônio líquido (R$): "))
        valor_divida = float(input("Valor dívida (R$): "))
        custo_patrimonio = float(input("Custo capital próprio (ex: 12): ")) / 100
        custo_divida = float(input("Custo da dívida (ex: 5): ")) / 100
        aliquota = float(input("Alíquota de imposto (ex: 25): ")) / 100

        resultado = FinancialAnalysis.weighted_average_cost_of_capital(
            valor_patrimonio, valor_divida, custo_patrimonio, custo_divida, aliquota)

        print_section("RESULTADO")
        print(f"Peso patrimônio: {format_percent(resultado['weight_equity'])}")
        print(f"Peso dívida: {format_percent(resultado['weight_debt'])}")
        print(f"WACC: {format_percent(resultado['wacc'])}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def analise_endividamento():
    """Análise de endividamento"""
    try:
        print_header("ANÁLISE DE ENDIVIDAMENTO")
        divida_total = float(input("Dívida total (R$): "))
        ativo_total = float(input("Ativo total (R$): "))
        patrimonio = float(input("Patrimônio líquido (R$): "))

        resultado = FinancialAnalysis.debt_ratio_analysis(
            divida_total, ativo_total, patrimonio)

        print_section("RESULTADO")
        print(f"Debt/Assets: {format_percent(resultado['debt_to_assets_ratio'])}")
        print(f"Debt/Equity: {format_percent(resultado['debt_to_equity_ratio'])}")
        print(f"Alavancagem: {resultado['financial_leverage']}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def analise_portfolio():
    """Análise de portfólio"""
    try:
        print_header("ANÁLISE DE PORTFÓLIO")
        num_investimentos = int(input("Número de investimentos: "))

        investimentos = []
        for i in range(num_investimentos):
            nome = input(f"Nome do investimento {i+1}: ")
            valor_inicial = float(input(f"  Valor inicial: "))
            valor_atual = float(input(f"  Valor atual: "))
            investimentos.append({
                'name': nome,
                'initial_value': valor_inicial,
                'current_value': valor_atual
            })

        resultado = FinancialAnalysis.portfolio_performance(investimentos)

        print_section("RESULTADO")
        print(f"Valor inicial total: {format_currency(resultado['total_initial_value'])}")
        print(f"Valor atual total: {format_currency(resultado['total_current_value'])}")
        print(f"Ganho total: {format_currency(resultado['total_gain'])}")
        print(f"Retorno: {format_percent(resultado['total_return_percent']/100)}")
        print(f"\nMelhor: {resultado['best_performer']}")
        print(f"Pior: {resultado['worst_performer']}")

    except ValueError:
        print("❌ Digite valores válidos!")
    except FinanceError as e:
        print(f"❌ Erro: {e}")

    input("\nPressione ENTER...")


def menu_conversao_taxas():
    """Menu de conversão de taxas"""
    while True:
        print_header("CONVERSÃO DE TAXAS")
        print("\n1. Anual para Mensal")
        print("2. Mensal para Anual")
        print("3. Taxa Efetiva")
        print("4. Voltar")
        print("="*70)

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            anual_mensal()
        elif opcao == "2":
            mensal_anual()
        elif opcao == "3":
            taxa_efetiva()
        elif opcao == "4":
            break
        else:
            print("❌ Opção inválida!")


def anual_mensal():
    """Converte anual para mensal"""
    try:
        taxa_anual = float(input("Taxa anual (ex: 12 para 12%): ")) / 100
        taxa_mensal = annual_to_monthly_rate(taxa_anual)

        print_section("RESULTADO")
        print(f"Taxa anual: {format_percent(taxa_anual)}")
        print(f"Taxa mensal equivalente: {format_percent(taxa_mensal)}")

    except ValueError:
        print("❌ Digite um valor válido!")

    input("\nPressione ENTER...")


def mensal_anual():
    """Converte mensal para anual"""
    try:
        taxa_mensal = float(input("Taxa mensal (ex: 1 para 1%): ")) / 100
        taxa_anual = monthly_to_annual_rate(taxa_mensal)

        print_section("RESULTADO")
        print(f"Taxa mensal: {format_percent(taxa_mensal)}")
        print(f"Taxa anual equivalente: {format_percent(taxa_anual)}")

    except ValueError:
        print("❌ Digite um valor válido!")

    input("\nPressione ENTER...")


def taxa_efetiva():
    """Calcula taxa efetiva"""
    try:
        taxa_nominal = float(input("Taxa nominal (ex: 12): ")) / 100

        print("\nFrequência de capitalização:")
        print("1. Anual")
        print("2. Semestral")
        print("3. Trimestral")
        print("4. Mensal")
        print("5. Diário")

        freq_opcao = input("Escolha: ").strip()
        frequencias = {"1": 1, "2": 2, "3": 4, "4": 12, "5": 365}
        frequencia = frequencias.get(freq_opcao, 12)

        taxa_efetiva = InterestCalculator.effective_rate(taxa_nominal, frequencia)

        print_section("RESULTADO")
        print(f"Taxa nominal: {format_percent(taxa_nominal)}")
        print(f"Capitalização: {frequencia}x ao ano")
        print(f"Taxa efetiva anual: {format_percent(taxa_efetiva)}")

    except (ValueError, KeyError):
        print("❌ Valores inválidos!")

    input("\nPressione ENTER...")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrompido.")
