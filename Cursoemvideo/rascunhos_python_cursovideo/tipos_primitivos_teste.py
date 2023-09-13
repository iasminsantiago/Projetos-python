n1 = input('Digite valor:')
n2 = input('Digite outro valor:')
soma = n1+n2
print(type(soma))  # soma está como string
print('A soma dos valores é:', soma)  # concatenou (juntar uma *string* com outra)
print(type(n1))  # está como string

# Fazer declarando pra input que n3 e n4 são inteiros:
n3 = int(input('Digite valor:'))
n4 = int(input('Digite outro valor:'))
sum = n3+n4 # com ou sem espaço entre o +, mostrou soma corretamente na linha abaixo
print('A soma dos valores é:', sum)
print(type(sum))  #soma estaá como int
print(type(n3))  # está como int, deu certo
print(type(n4))  # está como int, deu certo

# Mostrar a soma entre n3 e n4 vale ---    nao usar 'soma entre', n1, 'e', n2...., tem modo melhor:
print('A soma entre {} e {} vale {}'.format(n3,n4,sum))  # colocar espaço após ,:    note que qunado digita format(, ele ja destaca os {}
print('A soma entre {} e {} vale {}'.format(n3, n4, sum))  # mais bonito
print('A soma entre {0} e {1} vale {2}'.format(n3, n4, sum))  # usando números pra saber ordem ajuda e nao altera

# se nçao for usar a variável sum depois novamente, faz soma direto no .format
print('A soma entre {0} e {1} vale {2}'.format(n3, n4, n3+n4))

# para escolher casas decimas: pra 3 casas decimais, coloca na máscara :.3f   {:3f}
print('A divisão entre {} e {} é {:.3f}'.format(n3, n4, n3/n4))






