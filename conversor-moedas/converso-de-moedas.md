# Conversor de Moedas

Um conversor de moedas em tempo real com suporte a múltiplas moedas, integração com APIs de câmbio e interface CLI amigável. Suporta conversão entre mais de 10 moedas diferentes, incluindo Real Brasileiro (BRL), Dólar (USD), Euro (EUR), Libra (GBP) e outras.

<h1 align="center"> Características </h1>

- **Múltiplas Moedas Suportadas** (12+ moedas)
  - USD (Dólar Americano)
  - BRL (Real Brasileiro)
  - EUR (Euro)
  - GBP (Libra Esterlina)
  - JPY (Iene Japonês)
  - CHF (Franco Suíço)
  - AUD (Dólar Australiano)
  - CAD (Dólar Canadense)
  - E mais...

- **Conversão Flexível**
  - Entre duas moedas específicas
  - Para múltiplas moedas simultâneas
  - Com formatação monetária apropriada

- **Integração com APIs**
  - exchangerate-api.com (gratuita)
  - Fixer.io (com API key)
  - OpenExchangeRates.org (com API key)
  - Sistema de cache automático

- **Interface CLI Intuitiva**
  - Menu navegável
  - Tabelas formatadas
  - Informações detalhadas de cada moeda

- **Testes Completos**
  - 25+ testes unitários
  - Cobertura de casos normais e extremos
  - Validação de simetria de conversão

<h1 align="center"> Instalação </h1>

### Requisitos
- Python 3.7+
- pip

### Passos

1. Clone ou copie o repositório:
```bash
cd conversor-moedas
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

<h1 align="center"> Uso </h1>

### Executar a Aplicação

```bash
python main.py
```

### Menu Principal

A aplicação oferece um menu interativo com as seguintes opções:

1. **Converter Moeda**
   - Selecione moeda origem e destino
   - Digite o valor
   - Veja o resultado com taxa de câmbio

2. **Ver Taxa de Câmbio**
   - Informações específicas de uma moeda
   - Taxa de conversão para USD

3. **Tabela de Câmbio Completa**
   - Visualize todas as taxas
   - Base configurável (USD, BRL, EUR, etc.)

4. **Converter para Múltiplas Moedas**
   - Converta um valor para todas as moedas disponíveis
   - Visão geral de conversões

5. **Atualizar Taxas via API**
   - Busca taxas atualizadas em tempo real
   - Com fallback para cache local

6. **Informações de Moeda**
   - Detalhes completos de cada moeda
   - Exemplos de conversão

### Exemplos de Uso Programático

```python
from converter import CurrencyConverter
from api_handler import APIHandler

# Criar conversor
converter = CurrencyConverter()

# Conversão simples
resultado = converter.convert(100, 'BRL', 'USD')
print(f"R$ 100 = $ {resultado:.2f}")

# Converter para USD
em_dolar = converter.convert_to_usd(5000, 'BRL')
print(f"R$ 5000 = $ {em_dolar:.2f}")

# Converter de USD
em_reais = converter.convert_from_usd(500, 'BRL')
print(f"$ 500 = {converter.format_currency(em_reais, 'BRL')}")

# Obter taxa de câmbio
taxa = converter.get_rate('BRL')
print(f"1 USD = {taxa:.4f} BRL")

# Moedas suportadas
moedas = converter.get_supported_currencies()
print(f"Moedas disponíveis: {', '.join(moedas)}")

# Informações de moeda
info = converter.get_currency_info('BRL')
print(f"Código: {info['code']}")
print(f"Nome: {info['name']}")
print(f"Símbolo: {info['symbol']}")

# Conversão para múltiplas moedas
resumo = converter.get_conversion_summary(1, 'USD')
for moeda, valor in resumo.items():
    print(f"1 USD = {valor:.4f} {moeda}")

# Formatação monetária
formatado = converter.format_currency(1000.50, 'BRL')
print(formatado)  # R$ 1.000,50

# Atualizar taxas via API
api_handler = APIHandler()
dados = api_handler.update_with_cache_fallback()

# Tabela de câmbio
print(converter.get_exchange_table('USD'))
```

<h1 align="center"> Executar Testes </h1>

```bash
python -m unittest discover tests -v
```

Rodar teste específico:
```bash
python -m unittest tests.test_converter.TestCurrencyConverter.test_convert_usd_to_brl -v
```

<h1 align="center"> Estrutura do Projeto </h1>

```
conversor-moedas/
├──data/
      └── exchange_rates.json  
├── __init__.py
├──converter.py
├──converso-de-moedas.md  
├──api_handler.py
├──test_converter.py 
├── main.py              
├── requirements.txt              
```

<h1 align="center"> Classes e Métodos Principais </h1>

### CurrencyConverter

Classe principal para conversão de moedas.

**Métodos:**
- `convert(amount, from_currency, to_currency)` - Converte entre moedas
- `convert_to_usd(amount, from_currency)` - Converte para USD
- `convert_from_usd(amount, to_currency)` - Converte de USD
- `get_rate(currency)` - Obtém taxa de uma moeda
- `get_supported_currencies()` - Lista moedas suportadas
- `get_currency_info(currency)` - Informações da moeda
- `update_rate(currency, rate)` - Atualiza taxa
- `add_currency(currency, rate, name, symbol)` - Adiciona nova moeda
- `get_conversion_summary(amount, from_currency)` - Conversão múltipla
- `format_currency(amount, currency)` - Formata moeda
- `get_exchange_table(base_currency)` - Tabela completa
- `load_rates()` - Carrega taxas do arquivo
- `save_rates()` - Salva taxas no arquivo

### APIHandler

Gerencia integração com APIs de câmbio.

**Métodos:**
- `fetch_rates_exchangerate_api(base)` - Busca da exchangerate-api (gratuita)
- `fetch_rates_fixer_io(api_key, base)` - Busca do fixer.io
- `fetch_rates_openexchangerates(api_key, base)` - Busca do openexchangerates
- `save_to_cache(data)` - Salva dados em cache
- `load_from_cache()` - Carrega dados do cache
- `update_with_cache_fallback(api_key)` - Atualiza com fallback

## Integrações com APIs

### exchangerate-api.com (Recomendado)
- **Vantagem:** Gratuita, sem necessidade de chave
- **Desvantagem:** Limites de requisições
- **Uso Automático:** Já funciona sem configuração

### fixer.io
- **Requerimento:** API key necessária
- **Vantagem:** Mais atualizações
- **Uso:** Passe `api_key` ao usar `APIHandler`

### OpenExchangeRates.org
- **Requerimento:** API key necessária
- **Uso:** Passe `api_key` ao usar `APIHandler`


## Moedas Suportadas (12+)

| Código | Nome | Símbolo |
|--------|------|---------|
| USD | Dólar Americano | $ |
| BRL | Real Brasileiro | R$ |
| EUR | Euro | € |
| GBP | Libra Esterlina | £ |
| JPY | Iene Japonês | ¥ |
| CHF | Franco Suíço | CHF |
| AUD | Dólar Australiano | A$ |
| CAD | Dólar Canadense | C$ |
| MXN | Peso Mexicano | $ |
| CNY | Yuan Chinês | ¥ |
| INR | Rúpia Indiana | ₹ |
| RUB | Rublo Russo | ₽ |

<h1 align="center"> Exemplos de Casos de Uso </h1>

### Converter Viagem
```python
converter = CurrencyConverter()
gasto_brl = 5000  # Gasto na viagem em reais
gasto_usd = converter.convert_to_usd(gasto_brl, 'BRL')
print(f"Gasto em USD: {converter.format_currency(gasto_usd, 'USD')}")
```

### Comparar Preços Internacionais
```python
preco_amazon_us = 100  # USD
preco_amazon_br = converter.convert_from_usd(preco_amazon_us, 'BRL')
print(f"Preço no Brasil: {converter.format_currency(preco_amazon_br, 'BRL')}")
```

### Análise de Câmbio
```python
taxas = converter.get_conversion_summary(1, 'USD')
for moeda, taxa in sorted(taxas.items()):
    print(f"1 USD = {taxa:.4f} {moeda}")
```

## Notas Importantes

1. **Taxas Padrão:** Baseadas em valores aproximados. Sempre use APIs atualizadas para transações reais.
2. **Cache:** Atualizado automaticamente quando você escolhe "Atualizar taxas via API"
3. **Offline:** Funciona completamente offline usando dados em cache
4. **Precisão:** Recomenda-se atualizar taxas diariamente para maior precisão

----

<h3 aling="center"> Tecnologias </h3>

- Python 3.x

<h1 aling="center"> Autor </h1> 
<a href="https://github.com/ArthurHenrique-eng">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</a> 
