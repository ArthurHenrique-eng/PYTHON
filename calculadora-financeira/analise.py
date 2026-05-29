"""Módulo para análise geral de investimentos e inflação"""
from typing import List, Dict
from .juros import FinanceError


class FinancialAnalysis:
    """Análise financeira geral"""

    @staticmethod
    def real_return(nominal_return: float, inflation_rate: float) -> Dict:
        """
        Calcula rentabilidade real (descontada da inflação).

        Fórmula: r_real = ((1 + r_nominal) / (1 + inflação)) - 1

        Args:
            nominal_return: Rentabilidade nominal (em decimais)
            inflation_rate: Taxa de inflação (em decimais)

        Returns:
            Dicionário com análise
        """
        if nominal_return < -1 or nominal_return > 5:
            raise FinanceError("Rentabilidade parece inválida")
        if inflation_rate < 0 or inflation_rate > 1:
            raise FinanceError("Inflação deve estar entre 0 e 1")

        real_return = ((1 + nominal_return) / (1 + inflation_rate)) - 1

        return {
            'nominal_return': nominal_return,
            'inflation_rate': inflation_rate,
            'real_return': real_return,
            'nominal_percent': nominal_return * 100,
            'inflation_percent': inflation_rate * 100,
            'real_percent': real_return * 100
        }

    @staticmethod
    def future_value_with_inflation(present_value: float, inflation_rate: float,
                                   years: int) -> Dict:
        """
        Calcula valor futuro considerando inflação.

        Fórmula: VF_nominal = PV * (1 + inflação)^anos
                 VF_real = PV (poder de compra constante)

        Args:
            present_value: Valor presente
            inflation_rate: Taxa de inflação anual
            years: Número de anos

        Returns:
            Dicionário com cálculos
        """
        if present_value <= 0:
            raise FinanceError("Valor presente deve ser positivo")
        if inflation_rate < 0 or inflation_rate > 0.5:
            raise FinanceError("Inflação deve estar entre 0 e 50%")
        if years <= 0:
            raise FinanceError("Anos deve ser positivo")

        future_nominal = present_value * ((1 + inflation_rate) ** years)
        loss_of_value = future_nominal - present_value

        return {
            'present_value': present_value,
            'inflation_rate': inflation_rate,
            'years': years,
            'future_nominal_value': future_nominal,
            'loss_of_purchasing_power': loss_of_value,
            'loss_percentage': (loss_of_value / present_value) * 100
        }

    @staticmethod
    def minimum_return_needed(inflation_rate: float) -> Dict:
        """
        Calcula rentabilidade mínima necessária para não perder poder de compra.

        Args:
            inflation_rate: Taxa de inflação anual

        Returns:
            Rentabilidade mínima e análise
        """
        if inflation_rate < 0 or inflation_rate > 1:
            raise FinanceError("Inflação deve estar entre 0 e 1")

        minimum_return = inflation_rate

        return {
            'inflation_rate': inflation_rate,
            'inflation_percent': inflation_rate * 100,
            'minimum_return_needed': minimum_return,
            'minimum_return_percent': minimum_return * 100,
            'message': f"Para não perder poder de compra, você precisa ganhar pelo menos {minimum_return*100:.2f}% ao ano"
        }

    @staticmethod
    def weighted_average_cost_of_capital(equity_value: float, debt_value: float,
                                        equity_cost: float,
                                        debt_cost: float, tax_rate: float = 0) -> Dict:
        """
        Calcula WACC (Weighted Average Cost of Capital).

        Fórmula: WACC = (E/V) * r_e + (D/V) * r_d * (1 - T)

        Args:
            equity_value: Valor do patrimônio líquido
            debt_value: Valor da dívida
            equity_cost: Custo do capital próprio (%)
            debt_cost: Custo da dívida (%)
            tax_rate: Taxa de imposto (%)

        Returns:
            WACC e componentes
        """
        if equity_value < 0 or debt_value < 0:
            raise FinanceError("Valores não podem ser negativos")
        if equity_value + debt_value <= 0:
            raise FinanceError("Total deve ser positivo")

        total_value = equity_value + debt_value
        weight_equity = equity_value / total_value
        weight_debt = debt_value / total_value

        wacc = (weight_equity * equity_cost) + \
               (weight_debt * debt_cost * (1 - tax_rate))

        return {
            'equity_value': equity_value,
            'debt_value': debt_value,
            'total_value': total_value,
            'weight_equity': weight_equity,
            'weight_debt': weight_debt,
            'equity_cost': equity_cost,
            'debt_cost': debt_cost,
            'tax_rate': tax_rate,
            'wacc': wacc,
            'wacc_percent': wacc * 100
        }

    @staticmethod
    def debt_ratio_analysis(total_debt: float, total_assets: float,
                           total_equity: float) -> Dict:
        """
        Análise de índices de endividamento.

        Args:
            total_debt: Dívida total
            total_assets: Ativo total
            total_equity: Patrimônio líquido

        Returns:
            Índices de endividamento
        """
        if total_debt < 0 or total_assets <= 0 or total_equity < 0:
            raise FinanceError("Valores inválidos")

        debt_to_assets = total_debt / total_assets
        debt_to_equity = total_debt / total_equity if total_equity > 0 else 0
        equity_multiplier = total_assets / total_equity if total_equity > 0 else 0

        return {
            'total_debt': total_debt,
            'total_assets': total_assets,
            'total_equity': total_equity,
            'debt_to_assets_ratio': debt_to_assets,
            'debt_to_assets_percent': debt_to_assets * 100,
            'debt_to_equity_ratio': debt_to_equity,
            'debt_to_equity_percent': debt_to_equity * 100,
            'equity_multiplier': equity_multiplier,
            'financial_leverage': 'Alto' if debt_to_assets > 0.6 else 'Moderado'
            if debt_to_assets > 0.3 else 'Baixo'
        }

    @staticmethod
    def monthly_budget_analysis(income: float, expenses: List[Dict]) -> Dict:
        """
        Análise de orçamento mensal.

        Args:
            income: Renda mensal
            expenses: Lista de despesas com {'category': ..., 'value': ...}

        Returns:
            Análise de orçamento
        """
        if income <= 0:
            raise FinanceError("Renda deve ser positiva")

        total_expenses = sum(exp['value'] for exp in expenses)
        balance = income - total_expenses
        savings_rate = (balance / income) * 100 if income > 0 else 0

        categories = {}
        for exp in expenses:
            cat = exp['category']
            val = exp['value']
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += val

        category_percentages = {cat: (val / income) * 100
                               for cat, val in categories.items()}

        return {
            'income': income,
            'total_expenses': total_expenses,
            'balance': balance,
            'savings_rate': savings_rate,
            'expense_ratio': (total_expenses / income) * 100,
            'categories': categories,
            'category_percentages': category_percentages,
            'status': 'Superávit' if balance > 0 else 'Déficit' if balance < 0 else 'Equilibrado'
        }

    @staticmethod
    def portfolio_performance(investments: List[Dict]) -> Dict:
        """
        Análise de desempenho de portfólio.

        Args:
            investments: Lista com {'name': ..., 'initial_value': ..., 'current_value': ...}

        Returns:
            Análise agregada do portfólio
        """
        if not investments:
            raise FinanceError("Portfolio vazio")

        total_initial = sum(inv['initial_value'] for inv in investments)
        total_current = sum(inv['current_value'] for inv in investments)
        total_gain = total_current - total_initial
        total_return = (total_gain / total_initial) * 100 if total_initial > 0 else 0

        performance = []
        for inv in investments:
            initial = inv['initial_value']
            current = inv['current_value']
            gain = current - initial
            ret = (gain / initial) * 100 if initial > 0 else 0
            weight = (initial / total_initial) * 100

            performance.append({
                'name': inv['name'],
                'initial_value': initial,
                'current_value': current,
                'gain': gain,
                'return_percent': ret,
                'weight_percent': weight
            })

        # Ordenar por retorno
        performance_sorted = sorted(performance, key=lambda x: x['return_percent'],
                                   reverse=True)

        return {
            'total_initial_value': total_initial,
            'total_current_value': total_current,
            'total_gain': total_gain,
            'total_return_percent': total_return,
            'best_performer': performance_sorted[0]['name'],
            'worst_performer': performance_sorted[-1]['name'],
            'investments': performance_sorted
        }
