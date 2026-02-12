'''
Calculadora simples com validação de operação.
 Usei a variável "operacao_valida" como controle de fluxo.
Ela serve para garantir que o resultado só seja exibido
 se a operação for válida.
'''

# Isso é necessário porque nem todos os caminhos do código  criam a variável "resultado" (ex: divisão por zero ou operação inválida). 
# Sem esse controle, o programa poderia tentar imprimir uma variável não definida, causando erro (NameError).


a = float(input(" A: "))
b = float(input("B: "))
op = input("Operação (+ - * /): ").strip() # strip remove espaços em branco no começo ou fimd a string

operacao_valida = True
resultado = 0.0

'''
input guarda, por padrão, valores em string. Por isso, usamos "". 
'''
  
if op == "+":
  resultado = a+b

elif op == "-":
  resultado = a-b

elif op == "*":
  resultado = a*b
  
elif op == "/": 
  if b == 0:
    operacao_valida = False
    print("Operação náo válida. Divisão por 0 não permitida.")
  else:
    resultado = a/b

else:
  operacao_valida = False
  print("Operação inválida.")

if operacao_valida:
  print("Resultado = ", resultado)


# testei usar print sem if operacao_valida: para b == 0 e printou a mensagem de operaçao inválida, mas deu name error.
# Isso ocorreu pois, no caso de b == 0, resultaado nao foi definido e, ao final do codigo, pede-se para printar resultado. 
# Ja quando fazemos b != 0, não ha erro.
          

          
