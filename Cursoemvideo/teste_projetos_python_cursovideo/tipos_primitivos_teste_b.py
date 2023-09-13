#  se declarar como float, número 4 será mostrado como 4.0
n = float(input('Digite um número: '))
print(n)

# Há 2 modos de usar booleanos:
n = bool(input('Digite um valor: '))
print(n)
print(type(n))  # Se eu digitar vazio e dar enter, ele retorna como False. Tipo será bool
# ou por métodos de teste de tipo
n = input('Digite algo: ')
print(n.isnumeric())   #Se não for número, dá False
print(n.isalpha())  # Se não for letra, dá False.
# Mesmo que seja string, como 3a, de acordo com limitação de input, dará False. 3a não é alpha. é alphanumérico.
print(n.isalnum())  # Se é alfanumérico. Caracteres especiais como ! não são alfanuméricos
print(n.isupper())  #  Se tem somente letras maiúsculas
print(n.islower())  #  Se tem somente letras minúsculas
print(n.isprintable())  #  Se n pode ser impresso (???)
print(n.isspace())  #  Se tem espaços
print(n.istitle())  # Se é capitalizado


# para não quebrar a linha pois tem vários prints, usa , end= ' '
print('É alfanumumérico?', n.isalnum(), end=' ')
print('É em maiúsculo?', n.isupper())

# para quebrar a linha, usa \n  que significa new line
print('Está totalmente \nminúsculo?',n.islower())