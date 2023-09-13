# Programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome = input('Digite seu nome:')
print('OLá! É um prazer te conhecer,', nome)

# Outra forma: usa {}. Após a string, usa .format(nome)
print('OLá, {}! Prazer em te conhecer!'.format(nome))

print('OLá! Prazer em teu conhecer,{}'.format(nome), '!')  # Colocar 1 espaço após , e 2 espaços entre ) e #

# Melhor colocar ! dentro da frase ao invés de após variável nome: Menciona nome com o {} antes do !
# Assim, não haverá espaço entre nome e !
print("Olá! Prazer em te conhecer, {}!".format(nome))  # Agora ficou perfeito
