# 11: Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura=float(input('Largura da parede em metros:'))
altura=float(input('Altura da parede em metros:'))
area = altura*largura
print('Sua parede tem dimensões de {}x{} e área de {}m².\nVocê precisa de {:.2f}L de tinta par pintá-la.'.format(altura,largura,area, area/2))