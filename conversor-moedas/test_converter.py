import unittest
import json
from pathlib import Path
from src.converter import CurrencyConverter, ConversorError


class TestCurrencyConverter(unittest.TestCase):
    """Testes para o conversor de moedas"""

    def setUp(self):
        """Configura um conversor para os testes"""
        # Usa arquivo de teste se existir, senão cria um temporário
        current_dir = Path(__file__).parent.parent
        rates_file = current_dir / 'data' / 'exchange_rates.json'
        self.converter = CurrencyConverter(str(rates_file))

    def test_convert_usd_to_brl(self):
        """Testa conversão de USD para BRL"""
        resultado = self.converter.convert(1, 'USD', 'BRL')
        self.assertGreater(resultado, 0)

    def test_convert_brl_to_usd(self):
        """Testa conversão de BRL para USD"""
        resultado = self.converter.convert(5, 'BRL', 'USD')
        self.assertGreater(resultado, 0)
        self.assertAlmostEqual(resultado, 1, places=1)

    def test_convert_same_currency(self):
        """Testa conversão da mesma moeda"""
        resultado = self.converter.convert(100, 'USD', 'USD')
        self.assertAlmostEqual(resultado, 100)

    def test_convert_negative_amount(self):
        """Testa conversão com valor negativo"""
        with self.assertRaises(ConversorError):
            self.converter.convert(-100, 'USD', 'BRL')

    def test_convert_invalid_from_currency(self):
        """Testa conversão com moeda origem inválida"""
        with self.assertRaises(ConversorError):
            self.converter.convert(100, 'XXX', 'USD')

    def test_convert_invalid_to_currency(self):
        """Testa conversão com moeda destino inválida"""
        with self.assertRaises(ConversorError):
            self.converter.convert(100, 'USD', 'XXX')

    def test_convert_to_usd(self):
        """Testa atalho de conversão para USD"""
        resultado = self.converter.convert_to_usd(5, 'BRL')
        self.assertGreater(resultado, 0)

    def test_convert_from_usd(self):
        """Testa atalho de conversão de USD"""
        resultado = self.converter.convert_from_usd(1, 'EUR')
        self.assertGreater(resultado, 0)

    def test_get_rate(self):
        """Testa obtenção de taxa de câmbio"""
        taxa = self.converter.get_rate('BRL')
        self.assertGreater(taxa, 0)

    def test_get_rate_invalid_currency(self):
        """Testa obtenção de taxa com moeda inválida"""
        with self.assertRaises(ConversorError):
            self.converter.get_rate('XXX')

    def test_get_supported_currencies(self):
        """Testa lista de moedas suportadas"""
        moedas = self.converter.get_supported_currencies()
        self.assertGreater(len(moedas), 0)
        self.assertIn('USD', moedas)
        self.assertIn('BRL', moedas)

    def test_get_currency_info(self):
        """Testa informações de moeda"""
        info = self.converter.get_currency_info('BRL')
        self.assertEqual(info['code'], 'BRL')
        self.assertIn('name', info)
        self.assertIn('symbol', info)
        self.assertIn('rate_to_usd', info)

    def test_get_currency_info_invalid(self):
        """Testa informações de moeda inválida"""
        with self.assertRaises(ConversorError):
            self.converter.get_currency_info('XXX')

    def test_format_currency(self):
        """Testa formatação de moeda"""
        formatado = self.converter.format_currency(1000.50, 'BRL')
        self.assertIn('R$', formatado)
        self.assertIn('1000', formatado)

    def test_get_conversion_summary(self):
        """Testa resumo de conversão para múltiplas moedas"""
        resumo = self.converter.get_conversion_summary(1, 'USD')
        self.assertGreater(len(resumo), 0)
        self.assertIn('USD', resumo)
        self.assertIn('BRL', resumo)

    def test_conversion_symmetry(self):
        """Testa se conversão bidirecional é simétrica"""
        # 1 USD = X BRL, logo 1 BRL = 1/X USD
        usd_to_brl = self.converter.convert(1, 'USD', 'BRL')
        brl_to_usd = self.converter.convert(1, 'BRL', 'USD')

        produto = usd_to_brl * brl_to_usd
        self.assertAlmostEqual(produto, 1, places=2)

    def test_multiple_currencies_supported(self):
        """Testa se pelo menos 5 moedas estão suportadas"""
        moedas = self.converter.get_supported_currencies()
        self.assertGreaterEqual(len(moedas), 5)

    def test_brl_in_supported_currencies(self):
        """Testa se BRL está na lista de moedas suportadas"""
        moedas = self.converter.get_supported_currencies()
        self.assertIn('BRL', moedas)

    def test_large_amount_conversion(self):
        """Testa conversão de valores grandes"""
        resultado = self.converter.convert(1_000_000, 'USD', 'BRL')
        self.assertGreater(resultado, 1_000_000 * 5)  # BRL é mais de 5x mais de USD

    def test_small_amount_conversion(self):
        """Testa conversão de valores pequenos"""
        resultado = self.converter.convert(0.01, 'USD', 'BRL')
        self.assertGreater(resultado, 0)

    def test_get_exchange_table(self):
        """Testa geração de tabela de câmbio"""
        tabela = self.converter.get_exchange_table('USD')
        self.assertIn('USD', tabela)
        self.assertIn('BRL', tabela)


class TestCurrencyFormatting(unittest.TestCase):
    """Testes para formatação de moedas"""

    def setUp(self):
        current_dir = Path(__file__).parent.parent
        rates_file = current_dir / 'data' / 'exchange_rates.json'
        self.converter = CurrencyConverter(str(rates_file))

    def test_format_usd(self):
        """Testa formatação de USD"""
        formatado = self.converter.format_currency(100, 'USD')
        self.assertIn('$', formatado)

    def test_format_eur(self):
        """Testa formatação de EUR"""
        formatado = self.converter.format_currency(100, 'EUR')
        self.assertIn('€', formatado)

    def test_format_gbp(self):
        """Testa formatação de GBP"""
        formatado = self.converter.format_currency(100, 'GBP')
        self.assertIn('£', formatado)

    def test_format_preserves_amount(self):
        """Testa se formatação preserva o valor"""
        valor = 1234.56
        formatado = self.converter.format_currency(valor, 'BRL')
        self.assertIn('1234', formatado)


if __name__ == '__main__':
    unittest.main()
