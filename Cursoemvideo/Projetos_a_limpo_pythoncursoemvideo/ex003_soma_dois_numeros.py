# Crie um programa que leia 2 números e mostre a soma entre eles:
# Fazer declarando pra input que n3 e n4 são inteiros, senão essa função considera como string:
n3 = int(input('Digite valor:'))
n4 = int(input('Digite outro valor:'))
sum = n3+n4 # com ou sem espaço entre o +, mostrará soma corretamente na linha abaixo
print('A soma dos valores é:', sum)
print(type(sum))  #soma está como int

# Mostrar "a soma entre n3 e n4 vale ---"  nao usar 'soma entre', n1, 'e', n2...., há modo melhor:
print('A soma entre {} e {} vale {}'.format(n3, n4, sum))  # colocar espaço após as ,
print('A soma entre {0} e {1} vale {2}'.format(n3, n4, sum))  # usando números pra saber ordem ajuda e nao altera

#  Também, se não for usar sum novamente depois, não precisa criar sum. Soma direto:
print('A soma entre {0} e {1} vale {2}'.format(n3, n4, n3+n4))

# Se deseja escolher quantidade de casas decimas: para 3, coloca na máscara :.3f -> 3 casas decimais após o .
print('A divisão entre {} e {} é {:.3f}'.format(n3, n4, n3/n4))