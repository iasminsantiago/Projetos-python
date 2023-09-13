# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Informe a quantidade de km rodados:"))
dias = int(input("Informe a quantidade de dias de aluguel:"))

preco = 60*dias + 0.15*km
print('O total a pagar é R$ {:.2f}'.format(preco))
# sempre dividir em pequenos testes antes de fazer a linha com a resposta final
# (ele testou antes só a parte com 60*dias)
# dividir pra conquistar, cria pequenos módulos de funcionamento