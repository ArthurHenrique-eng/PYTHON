from imc import calcular_imc, classificar_imc
from interface import coletar_dados, exibir_resultado


def main():
    try:
        nome, altura, peso = coletar_dados()
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        exibir_resultado(nome, imc, classificacao)
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
