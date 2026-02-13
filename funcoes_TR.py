## Função de saudação
def saudar(nome):
  print(f"Olá, {nome}!")
  
saudar(input("Seu nome: "))


# Função calcular média
def calcular_media(a,b,c):
  return (a+b+c)/3.00
  
media = calcular_media(2.5, 6.9, 10)
print("Média: ", media)



# Função maior de 2 números
def maior(a,b):
  return a if a > b else b

a = int(input("Digite a: "))
b = int(input("Digite b: "))
print("O maior número é ", maior(a,b))
# É no print que a função será chamada. Aoinvés de eu definir valores de a e b, pedi ao usuário antes e usei os valores escolhidos no print.


# Função retornar se é par ou ímpar
# A função retornará se n % 2 é ugual a 0 ou não, sendo um resultado booleano
# A função é o primeiro bloco de código mas não é executada por isso. Somente no print ela foi chamada e será executada com n como parâmetro. 
def eh_par(n):
  return n % 2 == 0

n = int(input("Digite o número: "))
print("Par" if eh_par(n) else "Ímpar")


# Calculadora de operações 


