"""Módulo para análise de investimentos"""
from typing import List, Dict
import math
try:
    from .juros import FinanceError
except ImportError:
    from juros import FinanceError


class InvestmentAnalyzer:
    """Analisador de investimentos e projetos"""

    @staticmethod
    def npv(cash_flows: List[float], discount_rate: float) -> float:
        """
        Calcula o Valor Presente Líquido (NPV/VPL).

        Fórmula: VPL = Σ(CF_t / (1+i)^t) onde t = 0,1,2,...

        Args:
            cash_flows: Lista de fluxos de caixa (primeiro é investimento inicial)
            discount_rate: Taxa de desconto (ex: 0.1 para 10% a.a.)

        Returns:
            Valor Presente Líquido

        Raises:
            FinanceError: Se dados inválidos
        """
        if not cash_flows or len(cash_flows) < 2:
            raise FinanceError("Precisa de pelo menos 2 fluxos de caixa")
        if discount_rate < 0 or discount_rate > 1:
            raise FinanceError("Taxa de desconto deve estar entre 0 e 1")
        if cash_flows[0] >= 0:
            raise FinanceError("Primeiro fluxo (investimento) deve ser negativo")

        npv = 0
        for t, cf in enumerate(cash_flows):
            npv += cf / ((1 + discount_rate) ** t)

        return npv

    @staticmethod
    def irr(cash_flows: List[float], precision: float = 0.0001,
            max_iterations: int = 1000) -> float:
        """
        Calcula a Taxa Interna de Retorno (TIR/IRR).

        Usa método de Newton-Raphson para encontrar taxa onde NPV = 0.

        Args:
            cash_flows: Lista de fluxos de caixa
            precision: Precisão desejada
            max_iterations: Máximo de iterações

        Returns:
            Taxa Interna de Retorno

        Raises:
            FinanceError: Se não convergir ou dados inválidos
        """
        if not cash_flows or len(cash_flows) < 2:
            raise FinanceError("Precisa de pelo menos 2 fluxos de caixa")

        # Estimativa inicial
        rate = 0.1  # 10% inicial

        for _ in range(max_iterations):
            # Calcula NPV e sua derivada
            npv = sum(cf / ((1 + rate) ** t) for t, cf in enumerate(cash_flows))
            npv_derivative = sum(-t * cf / ((1 + rate) ** (t + 1))
                                for t, cf in enumerate(cash_flows))

            if abs(npv) < precision:
                return rate

            if abs(npv_derivative) < 1e-10:
                raise FinanceError("Não foi possível calcular TIR (derivada próxima a zero)")

            # Newton-Raphson
            rate = rate - npv / npv_derivative

            if rate < -0.99:  # Taxa não pode ser menor que -99%
                rate = -0.99

        raise FinanceError(f"TIR não convergiu após {max_iterations} iterações")

    @staticmethod
    def roi(initial_investment: float, final_value: float,
            years: int = 1) -> Dict[str, float]:
        """
        Calcula Retorno sobre Investimento (ROI).

        Fórmula: ROI = (Ganho Final - Investimento) / Investimento
                 ROI Anual = ((Final / Inicial)^(1/anos) - 1) * 100

        Args:
            initial_investment: Investimento inicial
            final_value: Valor final
            years: Número de anos

        Returns:
            Dicionário com ROI total e anual
        """
        if initial_investment <= 0:
            raise FinanceError("Investimento deve ser positivo")
        if final_value < 0:
            raise FinanceError("Valor final não pode ser negativo")
        if years <= 0:
            raise FinanceError("Anos deve ser positivo")

        gain = final_value - initial_investment
        roi_total = (gain / initial_investment) * 100

        if years > 0:
            roi_annual = ((final_value / initial_investment) ** (1 / years) - 1) * 100
        else:
            roi_annual = 0

        return {
            'initial_investment': initial_investment,
            'final_value': final_value,
            'gain': gain,
            'roi_total_percent': roi_total,
            'roi_annual_percent': roi_annual,
            'years': years
        }

    @staticmethod
    def payback_simple(cash_flows: List[float]) -> Dict:
        """
        Calcula Payback Simples (período de recuperação sem desconto).

        Args:
            cash_flows: Lista de fluxos de caixa

        Returns:
            Dicionário com informações de payback
        """
        if not cash_flows or len(cash_flows) < 2:
            raise FinanceError("Precisa de pelo menos 2 fluxos de caixa")

        accumulated = 0
        payback_period = None

        for t, cf in enumerate(cash_flows):
            accumulated += cf

            if accumulated >= 0 and payback_period is None:
                # Interpolação linear para maior precisão
                if t > 0:
                    previous_accumulated = accumulated - cf
                    if previous_accumulated < 0:
                        fraction = abs(previous_accumulated) / cf
                        payback_period = t - 1 + fraction
                    else:
                        payback_period = t
                else:
                    payback_period = 0

        return {
            'payback_period': payback_period,
            'has_payback': payback_period is not None,
            'type': 'Payback Simples'
        }

    @staticmethod
    def payback_discounted(cash_flows: List[float],
                          discount_rate: float) -> Dict:
        """
        Calcula Payback Descontado (período de recuperação com desconto).

        Args:
            cash_flows: Lista de fluxos de caixa
            discount_rate: Taxa de desconto

        Returns:
            Dicionário com informações de payback descontado
        """
        if not cash_flows or len(cash_flows) < 2:
            raise FinanceError("Precisa de pelo menos 2 fluxos de caixa")
        if discount_rate < 0 or discount_rate > 1:
            raise FinanceError("Taxa de desconto deve estar entre 0 e 1")

        accumulated = 0
        payback_period = None

        for t, cf in enumerate(cash_flows):
            discounted_cf = cf / ((1 + discount_rate) ** t)
            accumulated += discounted_cf

            if accumulated >= 0 and payback_period is None:
                if t > 0:
                    previous = accumulated - discounted_cf
                    if previous < 0:
                        fraction = abs(previous) / discounted_cf
                        payback_period = t - 1 + fraction
                    else:
                        payback_period = t
                else:
                    payback_period = 0

        return {
            'payback_period': payback_period,
            'has_payback': payback_period is not None,
            'discount_rate': discount_rate,
            'type': 'Payback Descontado'
        }

    @staticmethod
    def profitability_index(cash_flows: List[float],
                           discount_rate: float) -> float:
        """
        Calcula Índice de Rentabilidade (PI).

        Fórmula: PI = Σ(CF_t / (1+i)^t) / |Investimento Inicial|
                 PI > 1: Investimento viável
                 PI = 1: VPL = 0
                 PI < 1: VPL < 0

        Args:
            cash_flows: Lista de fluxos de caixa
            discount_rate: Taxa de desconto

        Returns:
            Índice de rentabilidade
        """
        if not cash_flows or len(cash_flows) < 2:
            raise FinanceError("Precisa de pelo menos 2 fluxos de caixa")

        initial_investment = abs(cash_flows[0])

        # Soma dos fluxos futuros descontados
        future_cash_flows = sum(cf / ((1 + discount_rate) ** t)
                               for t, cf in enumerate(cash_flows[1:], 1))

        return future_cash_flows / initial_investment

    @staticmethod
    def comparison_npv_irr(projects: Dict[str, List[float]],
                          discount_rate: float) -> Dict:
        """
        Compara múltiplos projetos usando NPV e TIR.

        Args:
            projects: Dicionário com nome do projeto e seus fluxos
            discount_rate: Taxa de desconto

        Returns:
            Análise comparativa de projetos
        """
        results = {}

        for project_name, cash_flows in projects.items():
            try:
                npv = InvestmentAnalyzer.npv(cash_flows, discount_rate)
                irr = InvestmentAnalyzer.irr(cash_flows)
                pi = InvestmentAnalyzer.profitability_index(
                    cash_flows, discount_rate)

                results[project_name] = {
                    'npv': npv,
                    'irr': irr,
                    'profitability_index': pi,
                    'recommended': npv > 0 and irr > discount_rate
                }
            except FinanceError as e:
                results[project_name] = {'error': str(e)}

        return results

    @staticmethod
    def break_even_analysis(fixed_costs: float, variable_cost_per_unit: float,
                           price_per_unit: float) -> Dict:
        """
        Análise do ponto de equilíbrio (Break Even).

        Fórmula: Q = CF / (P - CV)

        Args:
            fixed_costs: Custos fixos
            variable_cost_per_unit: Custo variável por unidade
            price_per_unit: Preço de venda por unidade

        Returns:
            Dicionário com análise
        """
        if fixed_costs < 0:
            raise FinanceError("Custos fixos não podem ser negativos")
        if variable_cost_per_unit < 0:
            raise FinanceError("Custo variável não pode ser negativo")
        if price_per_unit <= variable_cost_per_unit:
            raise FinanceError("Preço deve ser maior que custo variável")

        contribution_margin = price_per_unit - variable_cost_per_unit
        break_even_quantity = fixed_costs / contribution_margin
        break_even_revenue = break_even_quantity * price_per_unit

        return {
            'fixed_costs': fixed_costs,
            'variable_cost_per_unit': variable_cost_per_unit,
            'price_per_unit': price_per_unit,
            'contribution_margin': contribution_margin,
            'break_even_quantity': break_even_quantity,
            'break_even_revenue': break_even_revenue
        }
