# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada de 2 ou 3 casas decimais.
numero=int(input('Digite um número:'))
print('O dobro de {} vale {} \n O triplo de {} vale {} \n e a raiz quadrada de {} vale {:.3f}.'.format(numero, (numero*2), numero, (numero*3), numero, (pow(numero, (1/2)))))

# Outra forma, caso precice dos resultados depois como variáveis:
n = int(input('Digite um número:'))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(n, t, n, r))

#atenção: \nA  ** :.3f