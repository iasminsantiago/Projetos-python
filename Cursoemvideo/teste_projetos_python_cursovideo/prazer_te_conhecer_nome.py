# Programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome = input('Digite seu nome:')
print('OLá! É um prazer te conhecer,', nome)

# Outra forma: {} e após a atring, coloca .format(variavel)
print('OLá, {}! Prazer em te conhecer!'.format(nome))

print('OLá! Prazer em teu conhecer,{}'.format(nome),'!') # não esquecer {} na string
# colocar espaço após a ,, veja que está sublinhado
print('OLá! Prazer em teu conhecer,{}'.format(nome), '!')

# se colocar string depois do escrito da variavel, ficará com espaço não desejado após ela: , Ias !
# Melhor colocar o ! dentro do string grande, mencionando a variável com {} antes do !
print("Olá! Prazer em te conhecer, {}!".format(nome)) # agora ficou perfeito