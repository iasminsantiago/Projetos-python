# Diante de um pin correto, o usuário tem 3 tentarivas de inserir pins
# Vamos usar um contador para controlar as tentativas com for ou while

PIN_correto = 1234
tentativas = 0
liberado = False

# Só pediremos a tentativa 3 vezes. Assim, o input deve ficar dentro do while
# Será tentativas < 3 pois o prieiro passe foi em 0. A primeira tentativa terminou como tentativas 1. 
# Quando rodar o terceiro passe, tentativa terminará em 3, e próximo run em while não executa mais.
while tentativas <3:
  pin = int(input("Digite senha de 4 digitos: "))
  tentativas += 1
  if pin == PIN_correto:
    liberado = True
    break
  else:
    print(f"PIN incorreto, tentativa {tentativas} de 3.")

print("Acesso liberado" if liberado else "Acesso bloqueado.")


    

