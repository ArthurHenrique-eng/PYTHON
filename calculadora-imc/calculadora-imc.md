<<h1 align="center"> Calculadora IMC </h1>

Calculadora de Índice de Massa Corporal (IMC) desenvolvida em Python com arquitetura modular e separação de responsabilidades.

---

<h1 align="center"> Estrutura do projeto </h1>

```
calculadora-imc/
│
├── imc.py
├── interface.py
└── main.py
```

---

<h1 aling="center"> Como executar </h1>

**Pré-requisito:** Python 3.x instalado.

```bash
python main.py
```

---

<h1 aling="center"> Exemplo de uso </h1>

```
CALCULADORA IMC
Digite seu nome: Arthur
Digite sua altura em metros: 1.75
Digite seu peso em KG: 70.0

Arthur, seu IMC é 22.86 — com peso normal.
```

---

<h1 aling="center"> Tabela de classificação </h1> 

| IMC              | Classificação         |
|------------------|-----------------------|
| Até 18.5         | Abaixo do peso normal |
| 18.6 – 24.9      | Peso normal           |
| 25.0 – 29.9      | Sobrepeso             |
| 30.0 – 34.9      | Obesidade grau I      |
| 35.0 – 39.9      | Obesidade grau II     |
| 40.0 ou mais     | Obesidade grau III    |

---

<h1 aling="center"> Arquitetura </h1> 

O projeto segue o princípio de **separação de responsabilidades**:

- **`imc.py`** contém apenas lógica pura — sem `input()` ou `print()`. Pode ser importado e testado de forma independente.
- **`interface.py`** lida exclusivamente com a interface: coleta dados do usuário e exibe resultados.
- **`main.py`** importa os outros módulos e define o fluxo da aplicação.

Essa separação garante que, por exemplo, trocar o terminal por uma interface gráfica exija alterar apenas o `interface.py`.

---

<h3 aling="center"> Tecnologias </h3>

- Python 3.x

<h1 aling="center"> Autor </h1> 
<a href="https://github.com/ArthurHenrique-eng">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</a> 