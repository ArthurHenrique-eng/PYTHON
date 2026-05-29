def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")
    if peso <= 0:
        raise ValueError("Peso deve ser maior que zero.")

    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc <= 18.5:
        return "abaixo do peso normal"
    if imc <= 24.9:
        return "com peso normal"
    if imc <= 29.9:
        return "com sobrepeso"
    if imc <= 34.9:
        return "com obesidade grau I"
    if imc <= 39.9:
        return "com obesidade grau II"

    return "com obesidade grau III"
