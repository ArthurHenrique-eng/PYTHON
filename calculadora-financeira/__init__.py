"""Calculadora Financeira - Módulos de cálculos financeiros"""

from .juros import InterestCalculator, FinanceError
from .investimentos import InvestmentAnalyzer
from .emprestimos import LoanCalculator
from .analise import FinancialAnalysis
from .utils import (
    format_currency, format_percent, format_number,
    annual_to_monthly_rate, monthly_to_annual_rate,
    parse_percent, calculate_cagr, summary_table,
    print_amortization_schedule
)

__all__ = [
    'InterestCalculator',
    'InvestmentAnalyzer',
    'LoanCalculator',
    'FinancialAnalysis',
    'FinanceError',
    'format_currency',
    'format_percent',
    'format_number',
    'annual_to_monthly_rate',
    'monthly_to_annual_rate',
    'parse_percent',
    'calculate_cagr',
    'summary_table',
    'print_amortization_schedule'
]
