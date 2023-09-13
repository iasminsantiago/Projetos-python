# Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
celsius = float(input('Informe a temperatura em ºC: '))
fahren = celsius*9/5 + 32
print('A temperatura de {0} ºC corresponde a {1} ºF!'.format(celsius,fahren))
#se colocar nos {} 1 e 0 ao invés de 0 e 1, ele troca as variáveis de lugar
