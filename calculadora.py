print("CALCULADORA IMC")
nomePessoa = str(input("Digite seu nome e aperte ENTER:"))
alturaPessoa = float(input("Digite sua altura em metros com ponto decimal e aperte ENTER:"))
pesoPessoa = float(input("Digite seu peso em KG com ponto decimal e aperte ENTER:"))

IMC = pesoPessoa / (alturaPessoa ** 2)

if IMC <= 18.5:
    print(nomePessoa, "seu IMC é:", IMC, "e é considerado abaixo do peso normal!")

elif IMC >= 18.6 and IMC <= 24.9:
    print(nomePessoa, "seu IMC é:", IMC, "e é considerado com o peso normal!")

elif IMC >= 25.0 and IMC <= 29.9:
    print(nomePessoa, "seu IMC é:", IMC, "e é considerado com sobrepeso!")

elif IMC >= 30.0 and IMC <= 34.9:
    print(nomePessoa, "seu IMC é:", IMC, "e é considerado obesidade grau I!")

elif IMC >= 35.0 and IMC <= 39.9:
    print(nomePessoa, "seu IMC é:", IMC, "e é considerado obesidade grau II!")

elif IMC >= 40.0:
    print(nomePessoa, "seu IMC é:", IMC, "e é considerado obesidade grau III!")

else:
    print("Valores inválidos, reinicie o programa!")