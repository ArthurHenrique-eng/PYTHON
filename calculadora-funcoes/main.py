from functions import FirstDegreeFunction, SecondDegreeFunction, FunctionAnalyzer, FunctionError
from grapher import FunctionGrapher
import matplotlib.pyplot as plt


def clear_screen():
    """Limpa a tela do terminal"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal():
    """Menu principal da calculadora"""
    while True:
        print("\n" + "="*50)
        print("CALCULADORA DE FUNÇÕES MATEMÁTICAS")
        print("="*50)
        print("1. Função do Primeiro Grau (f(x) = ax + b)")
        print("2. Função do Segundo Grau (f(x) = ax² + bx + c)")
        print("3. Comparar Múltiplas Funções")
        print("4. Sair")
        print("="*50)

        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            menu_primeiro_grau()
        elif opcao == "2":
            menu_segundo_grau()
        elif opcao == "3":
            menu_comparar_funcoes()
        elif opcao == "4":
            print("\nAté logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


def menu_primeiro_grau():
    """Menu para função do primeiro grau"""
    print("\n" + "="*50)
    print("FUNÇÃO DO PRIMEIRO GRAU: f(x) = ax + b")
    print("="*50)

    try:
        a = float(input("Digite o coeficiente 'a': "))
        b = float(input("Digite o coeficiente 'b': "))

        func = FirstDegreeFunction(a, b)
        analise = FunctionAnalyzer.analyze_first_degree(a, b)

        print("\n" + "-"*50)
        print("ANÁLISE DA FUNÇÃO")
        print("-"*50)
        print(f"Função: {analise['function']}")
        print(f"Raiz: x = {analise['root']:.4f}")
        print(f"Coeficiente Angular (inclinação): {analise['slope']}")
        print(f"Intercepto Y: {analise['y_intercept']}")
        print(f"Crescente: {'Sim ↗' if analise['is_increasing'] else 'Não ↘'}")

        print("\n" + "-"*50)
        print("OPÇÕES")
        print("-"*50)
        print("1. Avaliar a função em um ponto")
        print("2. Visualizar gráfico")
        print("3. Voltar ao menu principal")
        print("-"*50)

        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            x = float(input("Digite o valor de x: "))
            resultado = func.evaluate(x)
            print(f"\n✓ f({x}) = {resultado:.4f}")
        elif opcao == "2":
            FunctionGrapher.plot_first_degree(a, b)
            plt.show()
        elif opcao != "3":
            print("❌ Opção inválida!")

    except FunctionError as e:
        print(f"❌ Erro: {e}")
    except ValueError:
        print("❌ Erro: Digite números válidos!")


def menu_segundo_grau():
    """Menu para função do segundo grau"""
    print("\n" + "="*50)
    print("FUNÇÃO DO SEGUNDO GRAU: f(x) = ax² + bx + c")
    print("="*50)

    try:
        a = float(input("Digite o coeficiente 'a': "))
        b = float(input("Digite o coeficiente 'b': "))
        c = float(input("Digite o coeficiente 'c': "))

        func = SecondDegreeFunction(a, b, c)
        analise = FunctionAnalyzer.analyze_second_degree(a, b, c)

        print("\n" + "-"*50)
        print("ANÁLISE COMPLETA DA FUNÇÃO")
        print("-"*50)
        print(f"Função: {analise['function']}")
        print(f"Δ (Delta): {analise['delta']:.4f}")
        print(f"Número de raízes reais: {analise['root_count']}")

        x1, x2 = analise['roots']
        if x1 is not None:
            if x1 == x2:
                print(f"Raiz dupla: x = {x1:.4f}")
            else:
                print(f"Raízes: x₁ = {x1:.4f}, x₂ = {x2:.4f}")

        vx, vy = analise['vertex']
        print(f"Vértice: ({vx:.4f}, {vy:.4f})")
        print(f"Eixo de simetria: x = {analise['axis_of_symmetry']:.4f}")
        print(f"Concavidade: {'Para cima ∩' if analise['concave_up'] else 'Para baixo ∪'}")

        if analise['minimum']:
            print(f"Valor mínimo: {analise['minimum']:.4f}")
        if analise['maximum']:
            print(f"Valor máximo: {analise['maximum']:.4f}")

        print("\n" + "-"*50)
        print("OPÇÕES")
        print("-"*50)
        print("1. Avaliar a função em um ponto")
        print("2. Visualizar gráfico")
        print("3. Voltar ao menu principal")
        print("-"*50)

        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            x = float(input("Digite o valor de x: "))
            resultado = func.evaluate(x)
            print(f"\n✓ f({x}) = {resultado:.4f}")
        elif opcao == "2":
            FunctionGrapher.plot_second_degree(a, b, c)
            plt.show()
        elif opcao != "3":
            print("❌ Opção inválida!")

    except FunctionError as e:
        print(f"❌ Erro: {e}")
    except ValueError:
        print("❌ Erro: Digite números válidos!")


def menu_comparar_funcoes():
    """Menu para comparar múltiplas funções"""
    print("\n" + "="*50)
    print("COMPARAR MÚLTIPLAS FUNÇÕES")
    print("="*50)
    print("1. Comparar funções do primeiro grau")
    print("2. Comparar funções do segundo grau")
    print("3. Voltar ao menu principal")
    print("="*50)

    opcao = input("Escolha uma opção (1-3): ").strip()

    if opcao == "1":
        comparar_primeiro_grau()
    elif opcao == "2":
        comparar_segundo_grau()


def comparar_primeiro_grau():
    """Compara funções do primeiro grau"""
    try:
        print("\nDigite os coeficientes das funções (deixe em branco para parar)")
        funcoes = []
        labels = []
        i = 1

        while True:
            print(f"\nFunção {i}:")
            a_str = input(f"  Coeficiente 'a': ").strip()
            if not a_str:
                break

            b_str = input(f"  Coeficiente 'b': ").strip()
            if not b_str:
                break

            a, b = float(a_str), float(b_str)
            func = FirstDegreeFunction(a, b)
            funcoes.append(lambda x, a=a, b=b: a*x + b)
            labels.append(f"f{i}(x) = {a}x + {b}")
            i += 1

        if funcoes:
            FunctionGrapher.plot_multiple_functions(funcoes, labels)
            plt.show()
        else:
            print("Nenhuma função informada!")

    except ValueError:
        print("❌ Erro: Digite números válidos!")


def comparar_segundo_grau():
    """Compara funções do segundo grau"""
    try:
        print("\nDigite os coeficientes das funções (deixe em branco para parar)")
        funcoes = []
        labels = []
        i = 1

        while True:
            print(f"\nFunção {i}:")
            a_str = input(f"  Coeficiente 'a': ").strip()
            if not a_str:
                break

            b_str = input(f"  Coeficiente 'b': ").strip()
            if not b_str:
                break

            c_str = input(f"  Coeficiente 'c': ").strip()
            if not c_str:
                break

            a, b, c = float(a_str), float(b_str), float(c_str)
            func = SecondDegreeFunction(a, b, c)
            funcoes.append(lambda x, a=a, b=b, c=c: a*x**2 + b*x + c)
            labels.append(f"f{i}(x) = {a}x² + {b}x + {c}")
            i += 1

        if funcoes:
            FunctionGrapher.plot_multiple_functions(funcoes, labels)
            plt.show()
        else:
            print("Nenhuma função informada!")

    except ValueError:
        print("❌ Erro: Digite números válidos!")


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrompido pelo usuário.")
