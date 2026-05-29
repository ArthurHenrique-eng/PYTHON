<h1 align="center"> Projetos Python </h1>

Repositorio com pequenos projetos em Python voltados para calculos, simulacoes e ferramentas de linha de comando. Cada pasta contem uma aplicacao independente, com seus proprios modulos e documentacao.

<h3 align="center"> Projetos incluidos </h3>

| Pasta | Projeto | Descricao |
| --- | --- | --- |
| `calculadora-financeira` | Calculadora Financeira | Calcula juros, investimentos, emprestimos, amortizacao, analise financeira e conversao de taxas. |
| `calculadora-funcoes` | Calculadora de Funcoes | Analisa funcoes do primeiro e segundo grau, calcula raizes, vertice, delta e gera graficos. |
| `calculadora-imc` | Calculadora IMC | Calcula o Indice de Massa Corporal e informa a classificacao do resultado. |
| `conversor-moedas` | Conversor de Moedas | Converte valores entre moedas usando taxas locais e integracao com API de cambio. |

<h3 align="center"> Estrutura geral </h3>

```text
PYTHON/
|-- calculadora-financeira/
|   |-- analise.py
|   |-- emprestimos.py
|   |-- investimentos.py
|   |-- juros.py
|   |-- main.py
|   |-- utils.py
|   `-- calculadora-financeira.md
|-- calculadora-funcoes/
|   |-- functions.py
|   |-- grapher.py
|   |-- main.py
|   `-- calculadora-funcoes.md
|-- calculadora-imc/
|   |-- imc.py
|   |-- interface.py
|   |-- main.py
|   `-- calculadora-imc.md
|-- conversor-moedas/
|   |-- api_handler.py
|   |-- converter.py
|   |-- data/
|   |   `-- exchange_rates.json
|   |-- main.py
|   |-- requirements.txt
|   |-- test_converter.py
|   `-- converso-de-moedas.md
`-- README.md
```

<h3 align="center"> Requisitos </h3>

- Python 3.x instalado
- `pip` para instalar dependencias quando necessario

O projeto `conversor-moedas` possui dependencia externa:

```bash
pip install -r conversor-moedas/requirements.txt
```

<h3 align="center"> Como executar </h3>

Entre na pasta do projeto desejado e execute o arquivo `main.py`.

### Calculadora Financeira

```bash
cd calculadora-financeira
python main.py
```

Funcionalidades principais:

- Juros simples, compostos e continuos
- Series de depositos e saques
- VPL, TIR, ROI, Payback e Break Even
- Emprestimos nos sistemas PRICE e SAC
- Analise financeira geral e conversao de taxas

Documentacao completa: [`calculadora-financeira/calculadora-financeira.md`](calculadora-financeira/calculadora-financeira.md)

### Calculadora de Funcoes

```bash
cd calculadora-funcoes
python main.py
```

Funcionalidades principais:

- Funcoes do primeiro grau
- Funcoes do segundo grau
- Calculo de delta, raizes e vertice
- Analise de crescimento, concavidade e pontos importantes
- Graficos com `matplotlib`

Documentacao completa: [`calculadora-funcoes/calculadora-funcoes.md`](calculadora-funcoes/calculadora-funcoes.md)

### Calculadora IMC

```bash
cd calculadora-imc
python main.py
```

Funcionalidades principais:

- Coleta de nome, altura e peso
- Calculo do IMC
- Classificacao do resultado conforme faixas de IMC

Documentacao completa: [`calculadora-imc/calculadora-imc.md`](calculadora-imc/calculadora-imc.md)

### Conversor de Moedas

```bash
cd conversor-moedas
pip install -r requirements.txt
python main.py
```

Funcionalidades principais:

- Conversao entre moedas
- Tabela de cambio
- Conversao para multiplas moedas
- Atualizacao de taxas via API
- Cache local em `data/exchange_rates.json`

Documentacao completa: [`conversor-moedas/converso-de-moedas.md`](conversor-moedas/converso-de-moedas.md)

<h3 align="center"> Testes </h3>

O projeto `conversor-moedas` possui arquivo de testes:

```bash
cd conversor-moedas
python -m unittest test_converter.py
```

Outras pastas podem receber testes futuramente seguindo o mesmo padrao com `unittest` ou `pytest`.

<h2 align="center"> Observacoes </h2>

- Cada pasta foi organizada como um projeto independente.
- Os arquivos `.md` dentro das pastas trazem mais detalhes sobre cada aplicacao.
- Alguns projetos usam apenas a biblioteca padrao do Python.
- O conversor de moedas usa `requests` para buscar dados externos de cambio.

<h1 aling="center"> Autor </h1> 
<a href="https://github.com/ArthurHenrique-eng">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</a> 
