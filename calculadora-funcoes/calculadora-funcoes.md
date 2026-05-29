# Calculadora de Funções Matemáticas

Uma aplicação Python completa para análise e visualização de funções matemáticas. Inclui suporte para funções do primeiro grau, segundo grau (Baskara), gráficos interativos e comparação entre múltiplas funções.

<h1 aling="center"> Características </h1> 

- **Funções do Primeiro Grau** (f(x) = ax + b)
  - Cálculo de raízes
  - Análise de coeficiente angular (inclinação)
  - Determinação se a função é crescente ou decrescente

- **Funções do Segundo Grau** (f(x) = ax² + bx + c)
  - Cálculo de Delta (Δ)
  - Resolução via fórmula de Baskara
  - Análise de vértice e eixo de simetria
  - Determinação de valores mínimos/máximos
  - Análise de concavidade

- **Visualização Gráfica**
  - Gráficos interativos com matplotlib
  - Marcação de raízes, vértices e pontos especiais
  - Comparação de múltiplas funções

- **Interface CLI Intuitiva**
  - Menu navegável
  - Validação de entrada
  - Tratamento de erros

- **Testes Automatizados**
  - Cobertura completa com unittest
  - Testes de casos normais e casos extremos

<h1 aling="center"> Instalação </h1> 

### Requisitos
- Python 3.7+

### Passos

1. Clone ou copie o repositório:
```bash
cd calculadora-funcoes
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

<h1 aling="center"> Uso </h1> 

### Executar a aplicação
```bash
python main.py
```

### Interface de Menu

A aplicação oferece um menu interativo com as seguintes opções:

1. **Função do Primeiro Grau**
   - Digite os coeficientes a e b
   - Visualize análise completa
   - Avalie a função em pontos específicos
   - Veja o gráfico

2. **Função do Segundo Grau**
   - Digite os coeficientes a, b e c
   - Obtenha análise de Delta, raízes, vértice, etc
   - Visualize o gráfico com marcações importantes

3. **Comparar Múltiplas Funções**
   - Compare até N funções no mesmo gráfico
   - Visualização comparativa

### Exemplo de Uso Programático

```python
from functions import FirstDegreeFunction, SecondDegreeFunction, FunctionAnalyzer
from grapher import FunctionGrapher
import matplotlib.pyplot as plt

# Primeiro Grau: f(x) = ax + b
func1 = FirstDegreeFunction(2, 3)
print(func1.evaluate(5))
print(func1.root())

# Segundo Grau: f(x) = x² - ax + b
func2 = SecondDegreeFunction(1, -5, 6)
print(func2.delta())
print(func2.roots())
print(func2.vertex())

# Análise completa
analise = FunctionAnalyzer.analyze_second_degree(1, -5, 6)
print(analise)

# Gráfico
FunctionGrapher.plot_second_degree(1, -5, 6)
plt.show()
```

<h1 aling="center"> Executar Testes </h1> 

```bash
python -m unittest discover tests
```

Ou rodar um teste específico:
```bash
python -m unittest tests.test_functions.TestFirstDegreeFunction
```

<h1 aling="center"> Estrutura do Projeto </h1> 

```
calculadora-funcoes/
├── __init__.py
├── calculadora-funcoes.md
├── functions.py
├──  grapher.py        # Geração de gráficos
└── main.py
```

<h1 aling="center"> Classes e Métodos </h1> 

### FirstDegreeFunction
Representa uma função do primeiro grau: f(x) = ax + b

**Métodos:**
- `evaluate(x)` - Avalia a função em um ponto
- `root()` - Retorna a raiz da função
- `slope()` - Retorna o coeficiente angular
- `y_intercept()` - Retorna o intercepto Y
- `is_increasing()` - Verifica se é crescente

### SecondDegreeFunction
Representa uma função do segundo grau: f(x) = ax² + bx + c

**Métodos:**
- `evaluate(x)` - Avalia a função em um ponto
- `delta()` - Calcula o discriminante Δ
- `roots()` - Retorna as raízes (usa Baskara)
- `vertex()` - Retorna o vértice da parábola
- `axis_of_symmetry()` - Retorna o eixo de simetria
- `is_concave_up()` - Verifica concavidade
- `minimum_value()` - Retorna valor mínimo (se a > 0)
- `maximum_value()` - Retorna valor máximo (se a < 0)
- `root_count()` - Retorna quantidade de raízes reais

### FunctionAnalyzer 
Realiza análise completa de funções

**Métodos Estáticos:**
- `analyze_first_degree(a, b)` - Análise completa do 1º grau
- `analyze_second_degree(a, b, c)` - Análise completa do 2º grau

### FunctionGrapher
Cria visualizações gráficas

**Métodos Estáticos:**
- `plot_first_degree(a, b, x_range, title)` - Gráfico de função linear
- `plot_second_degree(a, b, c, x_range, title)` - Gráfico de parábola
- `plot_multiple_functions(functions, labels, x_range, title)` - Comparação

<h1 aling="center"> Exemplos de Casos de Uso </h1> 

### Análise de Custos (Primeiro Grau)
```python
# Custo = 50 + 10x (50 fixo, 10 por unidade)
func = FirstDegreeFunction(10, 50)
custo_100_unidades = func.evaluate(100)
```

### Trajetória de Projétil (Segundo Grau)
```python
# h(t) = -ht² + 20t (altura em função do tempo)
func = SecondDegreeFunction(-5, 20, 0)
tempo_raiz = func.roots()  # Quando toca o solo
altura_max = fuc.maximum_value()  # Altura máxima
```

<h1 aling="center"> Conceitos Matemáticos </h1> 

### Função do Primeiro Grau
- **Forma Geral:** f(x) = ax + b
- **Raiz:** x = -b/a (onde a ≠ 0)
- **Crescente:** a > 0
- **Decrescente:** a < 0

### Função do Segundo Grau
- **Forma Geral:** f(x) = ax² + bx + c
- **Delta:** Δ = b² - 4ac
  - Δ > 0: 2 raízes reais distintas
  - Δ = 0: 1 raiz real (dupla)
  - Δ < 0: sem raízes reais
- **Baskara:** x = (-b ± √Δ) / 2a
- **Vértice:** V = (-b/2a, -Δ/4a)
- **Concavidade:** a > 0 (para cima), a < 0 (para baixo)

----

<h3 aling="center"> Tecnologias </h3>

- Python 3.x

<h1 aling="center"> Autor </h1> 
<a href="https://github.com/ArthurHenrique-eng">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</a> 
