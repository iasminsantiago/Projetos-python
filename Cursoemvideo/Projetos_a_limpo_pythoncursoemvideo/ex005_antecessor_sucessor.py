#  Faça um programa que leia um número inteiro e mostre na tela seu antecessor e seu sucessor
numero=int(input('Digite um número:'))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(numero,(numero-1),(numero+1)))
#  Como não precisarei usar os valores de antecessor e sucessor no futuro, sendo somente para mostrar na tela, não foi necessário criar variáveis deles
#  Quanto menos utilizar variáveis, mais memória terei disponível em meu dispositivo