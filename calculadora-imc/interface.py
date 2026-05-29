def coletar_dados():
    print("CALCULADORA IMC")
    nomePessoa = str(input("Digite seu nome e aperte ENTER:"))
    alturaPessoa = float(input("Digite sua altura em metros com ponto decimal e aperte ENTER:"))
    pesoPessoa = float(input("Digite seu peso em KG com ponto decimal e aperte ENTER:"))
    return nome, altura, peso


def exibir_resultado(nome, imc, classificacao):
    print(f"{nome}, seu IMC é {imc:.2f} — {classificacao}.")