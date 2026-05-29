"""Módulo para cálculos de juros simples e compostos"""
import math


class FinanceError(Exception):
    """Exceção para erros em cálculos financeiros"""
    pass


class InterestCalculator:
    """Calculadora de juros simples e compostos"""

    @staticmethod
    def simple_interest(principal: float, rate: float, time: float) -> dict:
        """
        Calcula juros simples.

        Fórmula: J = P * i * t
                 M = P + J = P(1 + i*t)

        Args:
            principal: Capital inicial (P)
            rate: Taxa de juros (i) - em decimais (ex: 0.05 para 5%)
            time: Período (t) - em anos

        Returns:
            Dicionário com valores calculados

        Raises:
            FinanceError: Se valores inválidos
        """
        if principal <= 0:
            raise FinanceError("Capital deve ser positivo")
        if rate < 0 or rate > 1:
            raise FinanceError("Taxa deve estar entre 0 e 1 (0 a 100%)")
        if time <= 0:
            raise FinanceError("Período deve ser positivo")

        interest = principal * rate * time
        amount = principal + interest

        return {
            'principal': principal,
            'rate': rate,
            'time': time,
            'interest': interest,
            'amount': amount,
            'type': 'Juros Simples'
        }

    @staticmethod
    def compound_interest(principal: float, rate: float, time: float,
                         compounds_per_year: int = 1) -> dict:
        """
        Calcula juros compostos.

        Fórmula: M = P(1 + i/n)^(n*t)
                 J = M - P

        Args:
            principal: Capital inicial (P)
            rate: Taxa de juros (i) - em decimais
            time: Período (t) - em anos
            compounds_per_year: Frequência de capitalização
                - 1: Anual
                - 2: Semestral
                - 4: Trimestral
                - 12: Mensal
                - 365: Diário

        Returns:
            Dicionário com valores calculados
        """
        if principal <= 0:
            raise FinanceError("Capital deve ser positivo")
        if rate < 0 or rate > 1:
            raise FinanceError("Taxa deve estar entre 0 e 1")
        if time <= 0:
            raise FinanceError("Período deve ser positivo")
        if compounds_per_year <= 0:
            raise FinanceError("Frequência deve ser positiva")

        amount = principal * ((1 + rate / compounds_per_year) **
                             (compounds_per_year * time))
        interest = amount - principal

        return {
            'principal': principal,
            'rate': rate,
            'time': time,
            'compounds_per_year': compounds_per_year,
            'interest': interest,
            'amount': amount,
            'type': 'Juros Compostos'
        }

    @staticmethod
    def continuous_compound(principal: float, rate: float, time: float) -> dict:
        """
        Calcula juros compostos contínuos.

        Fórmula: M = P * e^(i*t)

        Args:
            principal: Capital inicial
            rate: Taxa de juros
            time: Período

        Returns:
            Dicionário com valores calculados
        """
        if principal <= 0:
            raise FinanceError("Capital deve ser positivo")
        if rate < 0:
            raise FinanceError("Taxa não pode ser negativa")
        if time <= 0:
            raise FinanceError("Período deve ser positivo")

        amount = principal * math.exp(rate * time)
        interest = amount - principal

        return {
            'principal': principal,
            'rate': rate,
            'time': time,
            'interest': interest,
            'amount': amount,
            'type': 'Juros Compostos Contínuos'
        }

    @staticmethod
    def effective_rate(nominal_rate: float, compounds_per_year: int) -> float:
        """
        Calcula taxa efetiva (anual) a partir da taxa nominal.

        Fórmula: i_eff = (1 + i_nom/n)^n - 1

        Args:
            nominal_rate: Taxa nominal (em decimais)
            compounds_per_year: Frequência de capitalização

        Returns:
            Taxa efetiva anual
        """
        if nominal_rate < 0:
            raise FinanceError("Taxa não pode ser negativa")
        if compounds_per_year <= 0:
            raise FinanceError("Frequência deve ser positiva")

        return (1 + nominal_rate / compounds_per_year) ** compounds_per_year - 1

    @staticmethod
    def final_amount_series(monthly_deposit: float, rate: float, months: int,
                          deposit_type: str = 'end') -> dict:
        """
        Calcula valor final de uma série de depósitos iguais.

        Args:
            monthly_deposit: Valor do depósito periódico
            rate: Taxa por período (ex: 0.01 para 1% ao mês)
            months: Número de períodos
            deposit_type: 'end' (fim) ou 'beginning' (início do período)

        Returns:
            Dicionário com cálculos
        """
        if monthly_deposit <= 0:
            raise FinanceError("Depósito deve ser positivo")
        if rate < 0:
            raise FinanceError("Taxa não pode ser negativa")
        if months <= 0:
            raise FinanceError("Períodos deve ser positivo")

        if rate == 0:
            final_amount = monthly_deposit * months
        else:
            # Fórmula da série: FV = PMT * [((1+i)^n - 1) / i]
            factor = ((1 + rate) ** months - 1) / rate
            final_amount = monthly_deposit * factor

            if deposit_type == 'beginning':
                final_amount *= (1 + rate)

        total_deposited = monthly_deposit * months
        total_interest = final_amount - total_deposited

        return {
            'monthly_deposit': monthly_deposit,
            'rate': rate,
            'months': months,
            'deposit_type': deposit_type,
            'total_deposited': total_deposited,
            'total_interest': total_interest,
            'final_amount': final_amount
        }

    @staticmethod
    def present_value_series(monthly_withdrawal: float, rate: float,
                            months: int) -> float:
        """
        Calcula o valor presente necessário para uma série de saques.

        Fórmula: PV = PMT * [1 - (1+i)^(-n)] / i

        Args:
            monthly_withdrawal: Valor do saque periódico
            rate: Taxa por período
            months: Número de períodos

        Returns:
            Valor presente necessário
        """
        if monthly_withdrawal <= 0:
            raise FinanceError("Saque deve ser positivo")
        if rate < 0:
            raise FinanceError("Taxa não pode ser negativa")
        if months <= 0:
            raise FinanceError("Períodos deve ser positivo")

        if rate == 0:
            return monthly_withdrawal * months

        factor = (1 - (1 + rate) ** (-months)) / rate
        return monthly_withdrawal * factor
