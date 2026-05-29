from imc import calcular_imc, classificar_imc
from ui import coletar_dados, exibir_resultado


def main():
    print("CALCULADORA IMC")
    nome, altura, peso = coletar_dados()
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    exibir_resultado(nome, imc, classificacao)


if __name__ == "__main__":
    main()