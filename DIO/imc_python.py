# Criar um programa que calcule IMC (Índice de Massa Corpórea) utilizando a ferramenta Google cloud Shell Editor, utilizando a linguagem de programação Python
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif  imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"



interpretacao = interpretar_imc(imc)

print("Seu IMC é:", imc)
print("Você está classificado como:", interpretacao)