# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('QUal é o preço do produto? R$ '))
print('O produto que custava R${}, na promoção de 5% custará R${:.2f}.'.format(preco, preco*0.95))