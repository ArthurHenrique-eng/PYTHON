# PYTHON

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Interface-Tkinter-00d4ff?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Arquitetura-Clean%20Code-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge"/>
</p>

<p align="center">
Repositório com pequenos projetos em Python voltados para matemática, simulacoes e ferramentas de linha de comando. </br> Cada pasta contem uma aplicacao independente, com seus proprios modulos e documentacao.
</p>

---

## Projetos

| Pasta | Projeto | Descricao |
| --- | --- | --- |
| `calculadora-financeira` | Calculadora Financeira | Calcula juros, investimentos, emprestimos, amortizacao, analise financeira e conversao de taxas. |
| `calculadora-funcoes` | Calculadora de Funcoes | Analisa funcoes do primeiro e segundo grau, calcula raizes, vertice, delta e gera graficos. |
| `calculadora-imc` | Calculadora IMC | Calcula o Indice de Massa Corporal e informa a classificacao do resultado. |
| `conversor-moedas` | Conversor de Moedas | Converte valores entre moedas usando taxas locais e integracao com API de cambio. |

---

## Sobre o projeto

Este projeto são um conjunto de sistemas desenvolvidos em Python, com interface gráfica construída
usando `tkinter`. O objetivo foi praticar a organização de código em módulos com responsabilidades
bem definidas, seguindo princípios de **Clean Code** e separação de camadas.

---

## Funcionalidades de Cada Projeto

#### Calculadora Financeira

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

#### Calculadora de Funcoes

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

#### Calculadora IMC

```bash
cd calculadora-imc
python main.py
```

Funcionalidades principais:

- Coleta de nome, altura e peso
- Calculo do IMC
- Classificacao do resultado conforme faixas de IMC

Documentacao completa: [`calculadora-imc/calculadora-imc.md`](calculadora-imc/calculadora-imc.md)

#### Conversor de Moedas

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

---

## Estrutura do projeto

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

Cada módulo tem uma única responsabilidade — nenhum arquivo conhece mais do que precisa.

---

## Como rodar

Entre na pasta do projeto desejado e execute o arquivo `main.py`.

##### Requisitos
- Python 3.x instalado
- `pip` para instalar dependencias quando necessario
O projeto `conversor-moedas` possui dependencia externa:
```bash
pip install -r conversor-moedas/requirements.txt
```

##
| Tecnologia | Uso |
|---|---|
| [Python 3](https://www.python.org/) | Linguagem principal |

## Autor
[![GitHub](https://img.shields.io/badge/GitHub-ArthurHenrique--eng-181717?style=flat-square&logo=github)](https://github.com/ArthurHenrique-eng)
