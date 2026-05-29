
from typing import Union


def format_currency(value: float, currency: str = 'BRL') -> str:
    """
    Formata um valor como moeda.

    Args:
        value: Valor a formatar
        currency: Código da moeda

    Returns:
        String formatada
    """
    symbols = {
        'BRL': 'R$',
        'USD': 'US$',
        'EUR': '€',
        'GBP': '£'
    }

    symbol = symbols.get(currency, currency)
    return f"{symbol} {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_percent(value: float, decimal_places: int = 2) -> str:
    """
    Formata um valor como percentual.

    Args:
        value: Valor em decimais
        decimal_places: Casas decimais

    Returns:
        String formatada
    """
    return f"{value * 100:.{decimal_places}f}%"


def format_number(value: float, decimal_places: int = 2) -> str:
    """
    Formata um número com separadores.

    Args:
        value: Valor a formatar
        decimal_places: Casas decimais

    Returns:
        String formatada
    """
    return f"{value:,.{decimal_places}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def annual_to_monthly_rate(annual_rate: float) -> float:
    """
    Converte taxa anual para taxa mensal (capitalização composta).

    Args:
        annual_rate: Taxa anual (em decimais)

    Returns:
        Taxa mensal
    """
    return (1 + annual_rate) ** (1/12) - 1


def monthly_to_annual_rate(monthly_rate: float) -> float:
    """
    Converte taxa mensal para taxa anual.

    Args:
        monthly_rate: Taxa mensal (em decimais)

    Returns:
        Taxa anual
    """
    return (1 + monthly_rate) ** 12 - 1


def annual_to_daily_rate(annual_rate: float) -> float:
    """
    Converte taxa anual para taxa diária.

    Args:
        annual_rate: Taxa anual (em decimais)

    Returns:
        Taxa diária
    """
    return (1 + annual_rate) ** (1/365) - 1


def parse_percent(value: Union[str, float]) -> float:
    """
    Converte uma string de percentual para decimal.

    Args:
        value: Valor como string (ex: "5%") ou float

    Returns:
        Valor em decimais
    """
    if isinstance(value, str):
        value = value.strip().replace('%', '').strip()
        return float(value) / 100
    return float(value) / 100 if value > 1 else value


def calculate_cagr(beginning_value: float, ending_value: float,
                   years: int) -> float:
    """
    Calcula CAGR (Compound Annual Growth Rate).

    Fórmula: CAGR = (EV/BV)^(1/n) - 1

    Args:
        beginning_value: Valor inicial
        ending_value: Valor final
        years: Número de anos

    Returns:
        CAGR em decimais
    """
    if beginning_value <= 0:
        raise ValueError("Valor inicial deve ser positivo")
    if ending_value < 0:
        raise ValueError("Valor final não pode ser negativo")
    if years <= 0:
        raise ValueError("Anos deve ser positivo")

    return (ending_value / beginning_value) ** (1 / years) - 1


def summary_table(title: str, items: dict, currency: bool = False) -> str:
    """
    Cria uma tabela formatada de resumo.

    Args:
        title: Título da tabela
        items: Dicionário com itens
        currency: Se deve formatar como moeda

    Returns:
        String formatada
    """
    table = f"\n{'='*60}\n"
    table += f"{title.center(60)}\n"
    table += f"{'='*60}\n"

    for key, value in items.items():
        if isinstance(value, float):
            if currency:
                formatted_value = format_currency(value)
            else:
                formatted_value = format_number(value)
        else:
            formatted_value = str(value)

        table += f"{key:<35} {formatted_value:>20}\n"

    table += f"{'='*60}\n"
    return table


def print_amortization_schedule(schedule: list, limit: int = 12) -> str:
    """
    Formata tabela de amortização.

    Args:
        schedule: Lista de períodos
        limit: Máximo de períodos a mostrar

    Returns:
        String formatada
    """
    output = f"\n{'='*80}\n"
    output += "TABELA DE AMORTIZAÇÃO".center(80) + "\n"
    output += f"{'='*80}\n"
    output += f"{'Mês':<8}{'Pagamento':<18}{'Juros':<18}{'Amortização':<18}{'Saldo':<18}\n"
    output += f"{'-'*80}\n"

    # Mostrar alguns períodos selecionados
    total_periods = len(schedule)
    periods_to_show = min(limit, total_periods)

    if periods_to_show < total_periods:
        # Mostrar primeiros e últimos
        step = max(1, (total_periods - 2) // (periods_to_show - 2))
        indices = list(range(0, total_periods - 1, step)) + [total_periods - 1]
    else:
        indices = range(total_periods)

    for idx in indices:
        if idx < len(schedule):
            p = schedule[idx]
            output += (f"{p['month']:<8}"
                      f"{format_currency(p['payment']):<18}"
                      f"{format_currency(p['interest']):<18}"
                      f"{format_currency(p['amortization']):<18}"
                      f"{format_currency(p['remaining_balance']):<18}\n")

    output += f"{'='*80}\n"
    return output
