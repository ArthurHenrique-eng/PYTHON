# Calculadora Financeira Completa

Uma calculadora financeira profissional em Python com suporte a múltiplos cálculos: juros, investimentos, empréstimos, análise financeira e conversão de taxas. Ideal para análise de investimentos, planejamento financeiro e educação em finanças.

<h1 aling="center"> Características </h1>

### Cálculos de Juros
- **Juros Simples** - J = P * i * t
- **Juros Compostos** - M = P(1 + i/n)^(n*t)
- **Juros Contínuos** - M = P * e^(i*t)
- **Taxa Efetiva** - Conversão de taxa nominal para efetiva
- **Série de Depósitos** - Valor final de depósitos periódicos
- **Série de Saques** - Valor presente para saques periódicos

### Análise de Investimentos
- **VPL (Valor Presente Líquido)** - Análise da viabilidade de projetos
- **TIR (Taxa Interna de Retorno)** - Taxa de retorno do projeto
- **ROI (Retorno sobre Investimento)** - Percentual de retorno
- **Payback Simples** - Período de recuperação simples
- **Payback Descontado** - Período de recuperação descontado
- **Índice de Rentabilidade** - PI > 1 indica viabilidade
- **Break Even** - Ponto de equilíbrio
- **Comparação de Projetos** - Análise comparativa usando múltiplos indicadores

### Empréstimos e Financiamentos
- **Sistema PRICE** - Prestações iguais (mais usado)
- **Sistema SAC** - Amortização constante
- **Comparação PRICE vs SAC** - Qual sistema é mais vantajoso?
- **Tabela de Amortização** - Detalhado período a período
- **Refinanciamento** - Análise de viabilidade de refinanciar
- **Saldo Devedor** - Em qualquer período

### Análise Financeira Geral
- **Rentabilidade Real** - Descontando inflação
- **Valor Futuro com Inflação** - Perda de poder de compra
- **WACC** - Custo médio ponderado de capital
- **Índices de Endividamento** - Análise de estrutura de capital
- **Análise de Portfólio** - Desempenho de múltiplos investimentos
- **Análise Orçamentária** - Renda vs despesas

### Conversão de Taxas
- **Anual para Mensal** - Conversão com juros compostos
- **Mensal para Anual** - Conversão com juros compostos
- **Taxa Efetiva** - De qualquer frequência de capitalização
- **CAGR** - Taxa de crescimento anual composta

<h1 aling="center"> Instalação </h1>

### Requisitos
- Python 3.7+

### Passos

```bash
cd calculadora-financeira
```

Nenhuma dependência externa! Funciona com biblioteca padrão do Python.

<h1 aling="center"> Uso </h1>

### Executar a Aplicação

```bash
python main.py
```

<h1 aling="center"> Menu Principal </h1>

A aplicação oferece um menu intuitivo com as seguintes seções:

1. **Cálculos de Juros**
   - Juros simples, compostos, contínuos
   - Série de depósitos
   - Taxa efetiva

2. **Análise de Investimentos**
   - VPL e TIR
   - ROI e Payback
   - Break Even
   - Comparação de projetos

3. **Empréstimos e Financiamentos**
   - Sistema PRICE
   - Sistema SAC
   - Comparação e refinanciamento

4. **Análise Financeira Geral**
   - Rentabilidade real
   - Endividamento
   - Portfólio e orçamento

5. **Conversão de Taxas**
   - Conversões entre períodos
   - Taxa efetiva

<h1 aling="center"> Exemplos de Uso Programático </h1>

### Cálculos de Juros

```python
from src.juros import InterestCalculator

# Juros simples
resultado = InterestCalculator.simple_interest(1000, 0.05, 2)
print(f"Juros: R$ {resultado['interest']}")
print(f"Montante: R$ {resultado['amount']}")

# Juros compostos (mensal)
resultado = InterestCalculator.compound_interest(1000, 0.12, 1, 12)
print(f"Montante: R$ {resultado['amount']}")

# Taxa efetiva de taxa nominal
taxa_efetiva = InterestCalculator.effective_rate(0.12, 12)
print(f"Taxa efetiva anual: {taxa_efetiva * 100:.2f}%")
```

### Análise de Investimentos

```python
from src.investimentos import InvestmentAnalyzer

# Fluxos de caixa: investimento inicial + retornos anuais
cash_flows = [-10000, 3000, 3000, 3000, 3000, 3000]
taxa_desconto = 0.10

# VPL
vpl = InvestmentAnalyzer.npv(cash_flows, taxa_desconto)
print(f"VPL: R$ {vpl:.2f}")

# TIR
tir = InvestmentAnalyzer.irr(cash_flows)
print(f"TIR: {tir * 100:.2f}%")

# Payback
payback = InvestmentAnalyzer.payback_simple(cash_flows)
print(f"Payback: {payback['payback_period']:.2f} anos")

# ROI
roi = InvestmentAnalyzer.roi(10000, 15000, 3)
print(f"ROI anual: {roi['roi_annual_percent']:.2f}%")

# Break Even
be = InvestmentAnalyzer.break_even_analysis(5000, 10, 30)
print(f"Quantidade no break even: {be['break_even_quantity']:.0f} unidades")
```

### Empréstimos

```python
from src.emprestimos import LoanCalculator
from src.utils import annual_to_monthly_rate

# Sistema PRICE (prestações iguais)
price = LoanCalculator.price_amortization(
    10000, 
    annual_to_monthly_rate(0.12), 
    12
)
print(f"Prestação: R$ {price['monthly_payment']:.2f}")
print(f"Total de juros: R$ {price['total_interest']:.2f}")

# Sistema SAC (amortização constante)
sac = LoanCalculator.sac_amortization(
    10000, 
    annual_to_monthly_rate(0.12), 
    12
)
print(f"1ª Prestação: R$ {sac['first_payment']:.2f}")
print(f"Última Prestação: R$ {sac['last_payment']:.2f}")

# Comparação
comparacao = LoanCalculator.compare_systems(
    10000,
    annual_to_monthly_rate(0.12),
    12
)
print(f"Sistema mais barato: {comparacao['difference']['cheaper_system']}")

# Refinanciamento
refinanciamento = LoanCalculator.refinancing_analysis(
    8000, 
    6, 
    0.01, 
    0.008
)
print(f"Economia: R$ {refinanciamento['total_savings']:.2f}")
```

### Análise Financeira

```python
from src.analise import FinancialAnalysis

# Rentabilidade real
real = FinancialAnalysis.real_return(0.08, 0.03)
print(f"Rentabilidade real: {real['real_percent']:.2f}%")

# Valor futuro com inflação
futuro = FinancialAnalysis.future_value_with_inflation(1000, 0.05, 1)
print(f"Perda de poder de compra: R$ {futuro['loss_of_purchasing_power']:.2f}")

# WACC
wacc = FinancialAnalysis.weighted_average_cost_of_capital(
    50000, 30000, 0.12, 0.06, 0.25
)
print(f"WACC: {wacc['wacc_percent']:.2f}%")

# Análise de portfólio
investments = [
    {'name': 'Ações', 'initial_value': 5000, 'current_value': 6000},
    {'name': 'Renda Fixa', 'initial_value': 5000, 'current_value': 5300}
]
portfolio = FinancialAnalysis.portfolio_performance(investments)
print(f"Retorno total: {portfolio['total_return_percent']:.2f}%")
```

### Conversão de Taxas

```python
from src.utils import (
    annual_to_monthly_rate, 
    monthly_to_annual_rate,
    parse_percent,
    calculate_cagr
)

# Anual para mensal
taxa_mensal = annual_to_monthly_rate(0.12)  # 12% a.a.
print(f"Taxa mensal: {taxa_mensal * 100:.2f}%")

# Mensal para anual
taxa_anual = monthly_to_annual_rate(0.01)  # 1% a.m.
print(f"Taxa anual: {taxa_anual * 100:.2f}%")

# CAGR
cagr = calculate_cagr(1000, 1331, 3)
print(f"CAGR: {cagr * 100:.2f}%")

# Parser
taxa = parse_percent("5%")  # Converte "5%" para 0.05
```

<h1 aling="center"> Estrutura do Projeto </h1>

```
calculadora-financeira/
├── __init__.py
├── analise.py
├── calculadora-financeira.md
├── emprestimos.py
├── investimentos.py
├── juros.py
├── main.py
└── utils.py
```

<h1 aling="center"> Executar Testes </h1>

```bash
python -m unittest discover tests -v
```

Rodar teste específico:
```bash
python -m unittest tests.test_financeiro.TestInterestCalculator -v
```

<h1 aling="center"> Fórmulas Utilizadas </h1>

### Juros Simples
```
J = P × i × t
M = P(1 + i×t)
```

### Juros Compostos
```
M = P(1 + i/n)^(n×t)
```

### VPL (Valor Presente Líquido)
```
VPL = Σ(CF_t / (1+i)^t)
```

### TIR (Taxa Interna de Retorno)
```
Encontra i onde: Σ(CF_t / (1+i)^t) = 0
```

### PRICE
```
P = C × [i(1+i)^n] / [(1+i)^n - 1]
```

### SAC (Amortização Constante)
```
A = Valor / Períodos
Juros = Saldo × i
```

<h1 aling="center"> Casos de Uso </h1>

### 1. Análise de Empréstimo Imobiliário
```python
# Comparar PRICE vs SAC para hipoteca de 300.000
comparacao = LoanCalculator.compare_systems(
    300000,
    annual_to_monthly_rate(0.06),
    360  # 30 anos
)
```

### 2. Viabilidade de Projeto
```python
# Avaliar projeto com investimento inicial de 100.000
cash_flows = [-100000, 30000, 35000, 40000, 40000, 40000]
vpl = InvestmentAnalyzer.npv(cash_flows, 0.10)
tir = InvestmentAnalyzer.irr(cash_flows)
# Se VPL > 0 e TIR > 10%, o projeto é viável
```

### 3. Rentabilidade Real do Investimento
```python
# Aplicação rendeu 8% mas inflação foi 3%
real_return = FinancialAnalysis.real_return(0.08, 0.03)
```

### 4. Impacto da Inflação
```python
# Quanto 1.000 reais de hoje valerão em 5 anos com inflação de 5%?
futuro = FinancialAnalysis.future_value_with_inflation(1000, 0.05, 5)
```

<h1 aling="center"> Conceitos Educacionais </h1>

- **VPL > 0**: Investimento cria valor, é viável
- **TIR > Taxa de Desconto**: Investimento supera custo do capital
- **Payback Curto**: Recupera investimento rápido
- **PRICE**: Parcelas iguais, mais previsível
- **SAC**: Parcelas decrescentes, menos juros totais
- **Rentabilidade Real**: Descontar inflação da rentabilidade

<h1 aling="center"> Notas Importantes </h1>

1. **Sem Dependências Externas**: Funciona apenas com biblioteca padrão do Python
2. **Precisão**: Todos os cálculos usam matemática de ponto flutuante padrão
3. **Validação**: Todas as entradas são validadas com mensagens de erro claras
4. **Educacional**: Perfeito para aprender finanças com código real

----

<h3 aling="center"> Tecnologias </h3>

- Python 3.x

<h1 aling="center"> Autor </h1> 
<a href="https://github.com/ArthurHenrique-eng">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</a> 
