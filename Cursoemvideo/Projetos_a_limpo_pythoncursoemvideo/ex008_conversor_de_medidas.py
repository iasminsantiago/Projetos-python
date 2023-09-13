# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros sem casas decimais.
n = float(input('Digite uma distância em metros: '))
print('A medida de {:.0f}m corresponde a \n{:.0f}km \n{:.0f}hm \n{:.0f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm.'.format(n, (n/1000), (n/100), (n/10), (n*10), n*100, n*1000))

# Ou
print(f'A sua altura em mm é {n*1000:.5f} \n')
print(f'A sua altura em cm é {n*100} \n')
print(f'A sua altura em dm é {n*10:.5f} \n')
print(f'A sua altura em dam é {n/10} \n')
print(f'A sua altura em hm é {n/100} \n')
print(f'A sua altura em km é {n/1000:.4f} \n')

