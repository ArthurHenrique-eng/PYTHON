"""Módulo para cálculos de empréstimos e financiamentos"""
from typing import List, Dict
try:
    from .juros import FinanceError
except ImportError:
    from juros import FinanceError


class LoanCalculator:
    """Calculadora de empréstimos e financiamentos"""

    @staticmethod
    def simple_loan(principal: float, monthly_rate: float,
                   months: int) -> Dict:
        """
        Calcula financiamento simples (juros de forma simples).

        Args:
            principal: Valor do empréstimo
            monthly_rate: Taxa mensal (ex: 0.01 para 1%)
            months: Número de meses

        Returns:
            Dicionário com cálculos
        """
        if principal <= 0:
            raise FinanceError("Valor do empréstimo deve ser positivo")
        if monthly_rate < 0:
            raise FinanceError("Taxa não pode ser negativa")
        if months <= 0:
            raise FinanceError("Número de meses deve ser positivo")

        total_interest = principal * monthly_rate * months
        total_amount = principal + total_interest
        monthly_payment = total_amount / months

        return {
            'principal': principal,
            'monthly_rate': monthly_rate,
            'months': months,
            'total_interest': total_interest,
            'total_amount': total_amount,
            'monthly_payment': monthly_payment,
            'type': 'Empréstimo Simples'
        }

    @staticmethod
    def price_amortization(principal: float, monthly_rate: float,
                          months: int) -> Dict:
        """
        Calcula sistema de amortização PRICE (Prestações Iguais).

        Fórmula: P = C * [i(1+i)^n] / [(1+i)^n - 1]

        Args:
            principal: Valor do empréstimo
            monthly_rate: Taxa mensal
            months: Número de meses

        Returns:
            Dicionário com parcelas e amortização detalhada
        """
        if principal <= 0:
            raise FinanceError("Valor do empréstimo deve ser positivo")
        if monthly_rate < 0:
            raise FinanceError("Taxa não pode ser negativa")
        if months <= 0:
            raise FinanceError("Número de meses deve ser positivo")

        if monthly_rate == 0:
            monthly_payment = principal / months
        else:
            factor = (monthly_rate * (1 + monthly_rate) ** months) / \
                    ((1 + monthly_rate) ** months - 1)
            monthly_payment = principal * factor

        schedule = []
        remaining_balance = principal
        total_interest = 0

        for month in range(1, months + 1):
            interest = remaining_balance * monthly_rate
            amortization = monthly_payment - interest
            remaining_balance -= amortization
            total_interest += interest

            # Ajuste para arredondamento na última parcela
            if month == months:
                remaining_balance = 0
                amortization = monthly_payment - interest

            schedule.append({
                'month': month,
                'payment': monthly_payment,
                'interest': interest,
                'amortization': amortization,
                'remaining_balance': max(0, remaining_balance)
            })

        return {
            'principal': principal,
            'monthly_rate': monthly_rate,
            'months': months,
            'monthly_payment': monthly_payment,
            'total_paid': monthly_payment * months,
            'total_interest': total_interest,
            'schedule': schedule,
            'type': 'Sistema PRICE'
        }

    @staticmethod
    def sac_amortization(principal: float, monthly_rate: float,
                         months: int) -> Dict:
        """
        Calcula sistema de amortização SAC (Amortização Constante).

        A amortização é constante, mas os juros diminuem.

        Args:
            principal: Valor do empréstimo
            monthly_rate: Taxa mensal
            months: Número de meses

        Returns:
            Dicionário com parcelas e amortização detalhada
        """
        if principal <= 0:
            raise FinanceError("Valor do empréstimo deve ser positivo")
        if monthly_rate < 0:
            raise FinanceError("Taxa não pode ser negativa")
        if months <= 0:
            raise FinanceError("Número de meses deve ser positivo")

        amortization = principal / months
        schedule = []
        remaining_balance = principal
        total_interest = 0

        for month in range(1, months + 1):
            interest = remaining_balance * monthly_rate
            payment = amortization + interest
            remaining_balance -= amortization
            total_interest += interest

            schedule.append({
                'month': month,
                'payment': payment,
                'interest': interest,
                'amortization': amortization,
                'remaining_balance': max(0, remaining_balance)
            })

        return {
            'principal': principal,
            'monthly_rate': monthly_rate,
            'months': months,
            'constant_amortization': amortization,
            'first_payment': schedule[0]['payment'],
            'last_payment': schedule[-1]['payment'],
            'total_paid': sum(s['payment'] for s in schedule),
            'total_interest': total_interest,
            'schedule': schedule,
            'type': 'Sistema SAC'
        }

    @staticmethod
    def compare_systems(principal: float, monthly_rate: float,
                       months: int) -> Dict:
        """
        Compara sistemas de amortização PRICE vs SAC.

        Args:
            principal: Valor do empréstimo
            monthly_rate: Taxa mensal
            months: Número de meses

        Returns:
            Comparação entre os dois sistemas
        """
        price = LoanCalculator.price_amortization(
            principal, monthly_rate, months)
        sac = LoanCalculator.sac_amortization(
            principal, monthly_rate, months)

        return {
            'price': {
                'monthly_payment_first': price['monthly_payment'],
                'total_paid': price['total_paid'],
                'total_interest': price['total_interest']
            },
            'sac': {
                'monthly_payment_first': sac['first_payment'],
                'monthly_payment_last': sac['last_payment'],
                'total_paid': sac['total_paid'],
                'total_interest': sac['total_interest']
            },
            'difference': {
                'interest_difference': abs(price['total_interest'] -
                                          sac['total_interest']),
                'cheaper_system': 'SAC' if sac['total_interest'] <
                                 price['total_interest'] else 'PRICE'
            }
        }

    @staticmethod
    def remaining_balance_at_month(principal: float, monthly_rate: float,
                                  months: int, target_month: int,
                                  system: str = 'PRICE') -> Dict:
        """
        Calcula saldo devedor em um mês específico.

        Args:
            principal: Valor do empréstimo
            monthly_rate: Taxa mensal
            months: Número total de meses
            target_month: Mês desejado
            system: 'PRICE' ou 'SAC'

        Returns:
            Informações do saldo no mês desejado
        """
        if system.upper() == 'PRICE':
            amortization_data = LoanCalculator.price_amortization(
                principal, monthly_rate, months)
        elif system.upper() == 'SAC':
            amortization_data = LoanCalculator.sac_amortization(
                principal, monthly_rate, months)
        else:
            raise FinanceError("Sistema deve ser 'PRICE' ou 'SAC'")

        if target_month < 1 or target_month > months:
            raise FinanceError(f"Mês deve estar entre 1 e {months}")

        month_data = amortization_data['schedule'][target_month - 1]

        return {
            'system': system,
            'month': target_month,
            'payment': month_data['payment'],
            'interest': month_data['interest'],
            'amortization': month_data['amortization'],
            'remaining_balance': month_data['remaining_balance'],
            'total_paid_until_now': sum(s['payment']
                                        for s in amortization_data['schedule'][:target_month])
        }

    @staticmethod
    def refinancing_analysis(remaining_balance: float, remaining_months: int,
                            current_rate: float, new_rate: float) -> Dict:
        """
        Analisa opção de refinanciamento.

        Args:
            remaining_balance: Saldo devedor atual
            remaining_months: Meses ainda a pagar
            current_rate: Taxa atual (mensal)
            new_rate: Taxa nova (mensal)

        Returns:
            Análise de refinanciamento
        """
        if remaining_balance <= 0:
            raise FinanceError("Saldo devedor deve ser positivo")
        if remaining_months <= 0:
            raise FinanceError("Meses restantes deve ser positivo")

        # Cálculo com taxa atual
        current = LoanCalculator.price_amortization(
            remaining_balance, current_rate, remaining_months)

        # Cálculo com taxa nova
        new = LoanCalculator.price_amortization(
            remaining_balance, new_rate, remaining_months)

        savings = current['total_interest'] - new['total_interest']

        return {
            'current_rate': current_rate,
            'new_rate': new_rate,
            'rate_difference': new_rate - current_rate,
            'current_total_interest': current['total_interest'],
            'new_total_interest': new['total_interest'],
            'total_savings': savings,
            'percentage_savings': (savings / current['total_interest']) * 100
            if current['total_interest'] > 0 else 0,
            'worth_refinancing': savings > 0
        }
