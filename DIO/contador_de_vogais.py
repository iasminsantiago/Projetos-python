# CONTADOR DE VOGAIS NUMA STRING

# Complemente a função conta_vogais, que conta o número de vogais numa string de entrada. Podem ser minúsculas ou maiúsculas, sem acento,
# Defina o conjunto de vogais, crie um contador/variável para contar o número de vogais na string, começando com zero.
# Itere pelos caracteres da string, percorrendo cada caractere da string de entrada e checando se é uma das vogais de meu conjunto. Se caractere for uma das vogais, incrementar contador com +1

# Após percorrer toda a string, retorne o valor do contador, representante do número total de vogais nela.

# Entrada: uma só string contendo letras
# Saída: número inteiro que representa número de vogais da string de entrada.


def conta_vogais(texto):
    # TODO: Defina um conjunto de vogais, tanto minúsculas quanto maiúsculas:
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # TODO: Inicialize um contador para contar as vogais:
    contador = 0
    
    # Iteramos pelos caracteres da string
    for char in texto:
      # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
      if char in vogais:
        contador += 1
    
    # retorne valor do contador
    return contador

# Solicite ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")