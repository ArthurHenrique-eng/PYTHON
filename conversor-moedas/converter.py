import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple


class ConversorError(Exception):
    """Exceção para erros no conversor de moedas"""
    pass


class CurrencyConverter:
    """Conversor de moedas com suporte a múltiplas taxas de câmbio"""

    # Dicionário de moedas e seus nomes
    CURRENCY_NAMES = {
        'USD': 'Dólar Americano',
        'BRL': 'Real Brasileiro',
        'EUR': 'Euro',
        'GBP': 'Libra Esterlina',
        'JPY': 'Iene Japonês',
        'CHF': 'Franco Suíço',
        'AUD': 'Dólar Australiano',
        'CAD': 'Dólar Canadense',
        'MXN': 'Peso Mexicano',
        'CNY': 'Yuan Chinês',
        'INR': 'Rúpia Indiana',
        'RUB': 'Rublo Russo'
    }

    SYMBOLS = {
        'USD': '$',
        'BRL': 'R$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥',
        'CHF': 'CHF',
        'AUD': 'A$',
        'CAD': 'C$',
        'MXN': '$',
        'CNY': '¥',
        'INR': '₹',
        'RUB': '₽'
    }

    def __init__(self, rates_file: str = None):
        """
        Inicializa o conversor com taxas de câmbio.

        Args:
            rates_file: Caminho para arquivo JSON com taxas (padrão: data/exchange_rates.json)
        """
        self.rates = {}
        self.last_update = None

        if rates_file is None:
            # Use o diretório padrão
            current_dir = Path(__file__).parent.parent
            rates_file = current_dir / 'data' / 'exchange_rates.json'

        self.rates_file = rates_file
        self.load_rates()

    def load_rates(self) -> None:
        """Carrega as taxas de câmbio do arquivo JSON"""
        try:
            with open(self.rates_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.rates = data.get('rates', {})
                self.last_update = data.get('timestamp', None)

            if not self.rates:
                raise ConversorError("Nenhuma taxa de câmbio encontrada no arquivo")
        except FileNotFoundError:
            raise ConversorError(f"Arquivo de taxas não encontrado: {self.rates_file}")
        except json.JSONDecodeError:
            raise ConversorError(f"Erro ao decodificar JSON em: {self.rates_file}")

    def save_rates(self) -> None:
        """Salva as taxas de câmbio no arquivo JSON"""
        data = {
            'timestamp': datetime.now().timestamp(),
            'base': 'USD',
            'rates': self.rates
        }
        try:
            with open(self.rates_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.last_update = data['timestamp']
        except IOError as e:
            raise ConversorError(f"Erro ao salvar taxas: {e}")

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Converte um valor de uma moeda para outra.

        Args:
            amount: Valor a converter
            from_currency: Código da moeda origem (ex: 'BRL')
            to_currency: Código da moeda destino (ex: 'USD')

        Returns:
            Valor convertido

        Raises:
            ConversorError: Se a moeda não existir
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            raise ConversorError(f"Moeda origem '{from_currency}' não suportada")

        if to_currency not in self.rates:
            raise ConversorError(f"Moeda destino '{to_currency}' não suportada")

        if amount < 0:
            raise ConversorError("O valor deve ser positivo")

        # Converte para USD primeiro, depois para a moeda destino
        amount_in_usd = amount / self.rates[from_currency]
        result = amount_in_usd * self.rates[to_currency]

        return result

    def convert_to_usd(self, amount: float, from_currency: str) -> float:
        """Converte um valor para USD (atalho)"""
        return self.convert(amount, from_currency, 'USD')

    def convert_from_usd(self, amount: float, to_currency: str) -> float:
        """Converte um valor de USD para outra moeda (atalho)"""
        return self.convert(amount, 'USD', to_currency)

    def get_rate(self, currency: str) -> float:
        """
        Retorna a taxa de câmbio de uma moeda em relação ao USD.

        Args:
            currency: Código da moeda (ex: 'BRL')

        Returns:
            Taxa de câmbio (quanto dessa moeda = 1 USD)
        """
        currency = currency.upper()
        if currency not in self.rates:
            raise ConversorError(f"Moeda '{currency}' não suportada")

        return self.rates[currency]

    def get_supported_currencies(self) -> List[str]:
        """Retorna lista de moedas suportadas"""
        return sorted(list(self.rates.keys()))

    def get_currency_info(self, currency: str) -> Dict[str, str]:
        """
        Retorna informações sobre uma moeda.

        Args:
            currency: Código da moeda

        Returns:
            Dicionário com código, nome e símbolo
        """
        currency = currency.upper()

        if currency not in self.rates:
            raise ConversorError(f"Moeda '{currency}' não suportada")

        return {
            'code': currency,
            'name': self.CURRENCY_NAMES.get(currency, 'Desconhecida'),
            'symbol': self.SYMBOLS.get(currency, currency),
            'rate_to_usd': self.rates[currency]
        }

    def update_rate(self, currency: str, rate: float) -> None:
        """
        Atualiza a taxa de uma moeda.

        Args:
            currency: Código da moeda
            rate: Nova taxa
        """
        currency = currency.upper()

        if rate <= 0:
            raise ConversorError("Taxa deve ser maior que zero")

        self.rates[currency] = rate
        self.save_rates()

    def add_currency(self, currency: str, rate: float, name: str = "", symbol: str = "") -> None:
        """
        Adiciona uma nova moeda ao conversor.

        Args:
            currency: Código da moeda
            rate: Taxa de câmbio
            name: Nome da moeda
            symbol: Símbolo da moeda
        """
        currency = currency.upper()

        if currency in self.rates:
            raise ConversorError(f"Moeda '{currency}' já existe")

        self.rates[currency] = rate
        if name:
            self.CURRENCY_NAMES[currency] = name
        if symbol:
            self.SYMBOLS[currency] = symbol

        self.save_rates()

    def get_conversion_summary(self, amount: float, from_currency: str) -> Dict[str, float]:
        """
        Retorna conversão de um valor para todas as moedas suportadas.

        Args:
            amount: Valor a converter
            from_currency: Moeda origem

        Returns:
            Dicionário com conversões para todas as moedas
        """
        from_currency = from_currency.upper()

        if from_currency not in self.rates:
            raise ConversorError(f"Moeda '{from_currency}' não suportada")

        summary = {}
        for currency in self.get_supported_currencies():
            summary[currency] = self.convert(amount, from_currency, currency)

        return summary

    def format_currency(self, amount: float, currency: str) -> str:
        """
        Formata um valor com a moeda apropriada.

        Args:
            amount: Valor
            currency: Código da moeda

        Returns:
            String formatada (ex: "R$ 100,50")
        """
        currency = currency.upper()

        if currency not in self.rates:
            raise ConversorError(f"Moeda '{currency}' não suportada")

        symbol = self.SYMBOLS.get(currency, currency)
        return f"{symbol} {amount:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def get_exchange_table(self, base_currency: str = 'USD') -> str:
        """
        Gera uma tabela de taxas de câmbio.

        Args:
            base_currency: Moeda base para a tabela

        Returns:
            String formatada com tabela de câmbio
        """
        base_currency = base_currency.upper()

        if base_currency not in self.rates:
            raise ConversorError(f"Moeda base '{base_currency}' não suportada")

        table = f"\n{'='*70}\n"
        table += f"TABELA DE CÂMBIO (Base: {base_currency})\n"
        table += f"{'='*70}\n"
        table += f"{'Moeda':<10} {'Nome':<25} {'Taxa':<15} {'Símbolo':<10}\n"
        table += f"{'-'*70}\n"

        for currency in self.get_supported_currencies():
            rate = self.convert(1, base_currency, currency)
            name = self.CURRENCY_NAMES.get(currency, 'Desconhecida')
            symbol = self.SYMBOLS.get(currency, currency)
            table += f"{currency:<10} {name:<25} {rate:>14.4f} {symbol:<10}\n"

        table += f"{'='*70}\n"

        if self.last_update:
            last_update_date = datetime.fromtimestamp(self.last_update).strftime('%d/%m/%Y %H:%M:%S')
            table += f"Última atualização: {last_update_date}\n"

        return table
