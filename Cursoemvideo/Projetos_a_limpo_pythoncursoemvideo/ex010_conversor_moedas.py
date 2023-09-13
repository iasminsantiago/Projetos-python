# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#  Considere US$ 1,00 = R$ 4,99

reais=float(input('Quanto dinheiro você tem n carteira? R$ ')) # Digitar o R$ para evitar o usuário digital o R$ e dar erro
dolares=reais/4.99
print('Com R$ {:.2f}, você pode comprar US${:.2f} dólares'.format(reais,dolares))