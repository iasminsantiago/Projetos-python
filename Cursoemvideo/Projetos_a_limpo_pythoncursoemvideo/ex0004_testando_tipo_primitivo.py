algo = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(algo))  #  sempre mostrará como string pois não fiz conversão
# Para ter todos os prints na mesma linha, usa ,end=' '
print('Só tem espaços? ', algo.isspace(), end=' ')
# para quebrar a linha, usa \n  que significa new line
print('Então, \nÉ um número? ', algo.isnumeric())

print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())  #  A1 dá true pois só há 1 letra e está capitalizada, Ab1 dá false
print('Está em minúsculas?', algo.islower())
print('Está capitalizado?', algo.istitle())


