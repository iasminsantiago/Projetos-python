# não há limite de quantidade de notas. O usuário informará quando parar digitando -1.
# assim, criaremos uma variável para acumular os valores de nota informados e outra variável para contar a quantidade de notas informadas


# Tye Hinting:
soma: float = 0.00
quantidade: int = 0 # contagem é absoluta, não tem decimais


# Devemos criar um loop, Se não usarmos while, ele só perguntará a nota 1 vez.
# Se digitado -1, ele sai do loop e nem aumenta/conta a mais na variável quantidade.
# Em if, não usaremos "-1" e sim -1, pois convertemos a string do input para float. 
# Como nota é numero, não podemos aplicar strip(), que só vale para strings.
while True:
  nota: float = float(input("Digite uma nota (ou -1 para parar): "))
  if nota == -1:
    break
  soma += nota
  quantidade +=  1


# se a quantidade for 0, devemos devemos printar que nenhuma nota foi informada, antes de mostrar a média. Se vier depois, o print da média mostrará 0.
if quantidade <= 0:
  print("Nenhuma nota foi informada.")
else:
  print(f"A média das {quantidade} notas digitadas foi {soma/quantidade}.")

# Para exibir a quantidade de notas sem casas decimais, posso:
# formatar com :.0f
# formatar com {int(quantidade)}
# no inicio, informar quantidade = 0 ao invés de 0.0

