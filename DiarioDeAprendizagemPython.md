## DIFERENÇAS
- snake_case
- Tem PIP
- não finaliza com ;
- não tem main padrão, este é só uma boa prática

## COMENTÁRIO
usa # para inline

ou """ texto """

## FACILIDADES
- ("\nQuebra linha")
- ("\tDá tab na exibição") (tabulação)
- ```python
  print(""sem quebra ", end="")
  print("de linha, mesmo havendo 2 prints", end="")
  '''

## PRINT
- se refere o fato histórico de que, nos primeiros computadores, os terminais nao mostravam o resultado em tela: literalmente o imprimiam, para os mostrar em folha de papel.

## CASTING
- converter valor de um tipo em outro
- float -> int
- mostar o valor em float e em int. 
```python
valor = 7.9
inteiro = int(valor)
print("float: ", valor)
print("int: ", inteiro)
```
- Se eu converter e armazenar o resultado na mesma variável, perco o valor original.
- Depois que converter, não posso usar mais o valor como float.
- Se eu ainda precisar do valor original, crio outra variável para armazenar o resultado da conversão.


## PIP
- Preferred installer program
- gerencia pacotes do python 
- É um programa do ecossistema Python, NÃO tem no java (Java usa Maven/Gradle).
- Usamos no terminal (do windows, do vs code)
```python
  pip install pacote_tal
```
 
  
Funções:
- Instalar bibliotecas de terceiros
- Atualizar bibliotecas
- Remover bibliotecas


## __name__ e __main__
```python
# script.py ----
def main():
  print("olá")

if __name__ = "__main__":
  main()
```
- __name__ é uma variável especial do Python.
- Quando o arquivo é executado diretamente, o valor de __name__ é "__main__", e Olá será printado. 
- Quando o arquivo é importado em outro arquivo, o valor de __name__ passa a ser o nome do módulo, não executando main() e nem printando Olá.
- Se eu rodar script.py diretamente → ele executa main().
- Se eu importar script.py em outro arquivo → o main() não será executado automaticamente.
- Isso evita que código seja executado sem intenção quando estamos apenas importando funções.
- Main é apenas uma função que nomemei como main, não tem o mesmo papel obrigatório que no Java, É apenas uma boa prática, para mostrar o ponto de entrada/começo do meu programa.


## INTERPOLAR
- interpolar = inserir valores dentro de uma string.
- inserir ou colocar elementos entre outros já existentes
- {} é usado para interpolar, junto com f-string.
  
 ```python
nome = input("Digite idade: ")
idade = int(input( "digite nome: ")
printf("Olá, {nome}, você tem {idade} anos!")
```

- "Olá" e "você tem" são strings estáticas, aparecem exatamente onde descritas
- {nome} e {idade} são substituídos pelos valores das variáveis.


## ITERAÇÃO
- iterar = repetir um processo várias vezes
- - em cálculo numérico de engenharia básica, vimos iteração como um processo de pegar um valor inicial , aplicar uma formula, pegar o resultado, aplciar a formaula novamente e repetir até o resultado estar próximo da resposta desejada. Cada passo é uma iteração.
  - assimiladamente, em programaçao, iterar é repetir um processo (print(i)) várias vezes -> repetir um bloco de código
 - for i in range (inicio, parada)
  ``` python
  for i in range(1,6):
    print(i)
  ```


## BREAK
- Para um loop que não tem limite/parada definido
- loop infinito, pois o True não mudará sozinho, a menos que seja interrompido por um comando interno.
  ```python
  while True:
    txt = input("Digite algo (ou "sair"): ")
    if txt.strip().lower() == "sair":
      break
    print("Você digitou: ", txt)
  ```
- o bloco de if contendo break faz o pc não ficar num ciclo eterno
- usado em chatbots ("digite sair")
  - se o comando não foi "sair", break é ignorado e o cursor volta ao while true
    - usamos lower para respostas SAIR, Sair etc serem transformadas/normalizadas/padronizadas como sair


## FUNÇÕES
- escopo: variáveis dentro da função, só funcionam quando estou rodando a funçao em si
- atributos:
- parâmetros: entradas que funçao recebe para aplicar como valor de suas variáveis (ex.: a, b, c)
- aplicadas em validação de dados (CPF), padronizaçao de saídas (aplicando casting, lower() no return), cálculos reutilizáveis (média), organização por etapas (ler dados, processar, exibir resultados)



## 
---
### Fontes
Treina Recife - Portal do Aluno
