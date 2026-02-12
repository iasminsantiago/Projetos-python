# não há limite de quantidade de notas. O usuário informará quando parar digitando -1.
# assim, criaremos uma variável para acumular os valores de nota informados e outra variável para contar a quantidade de notas informadas

soma = 0.00
quantidade = 0.00

# devemos criar um loop, Se não usarmos while, ele só perguntará a nota 1 vez.
while True:
  nota = float(input("Digite uma nota (ou "-1" para parar): ")):
    if nota == "-1":
      break
      # se digitado -1, ele sai do loop e nem aumenta/conta a mais na variável quantidade
    soma += nota
    quantidade +=  1

# se a quantidade for 0, devemos devemos printar que nenhuma nota foi informada, antes de mostrar a média. Se vier depois, o print da média mostrará 0.
if quantidade < 0:
  print("Nenhuma nota foi informada.")
else:
  printf("A média das {quantidade} notas digitadas foi {soma/quantidade}.")
