## CASTING
float -> int
mostar o valor em float e em int. 
valor = 7.9
inteiro = int(valor)
print("float: ", valor)
print("int: ", inteiro)


Se converter valor e armazenar int nela mesma, depois que converter, não posso usar mais o valor como float. Se precisar usa-lo, depois de converter não mudo variável diretamente. Crio outra variável que armazene o resultado.


## PIP
- Preferred installer program
- gerencia e instala bibliotecas de terceiros
- é programa do python, NÃO tem no java. Usamos no terminal (do windows, do vs code)
- - pip install jacoteXY.py


## __name__ e __main__
script.py ----
def main():
  print("olá")

if __name__ = "__main__":
  main()

se o nome do arquivo for main, ele executa o codigo main e printa Olá.
Mas quando importo meu arquivo (script.py) em outro, com nome de arquivo diferente do meu, ele não executará o main() automaticamente, não printando Olá.
Isso impede que meu código seja executado autoamaticamente num código em que a pessoa apenas queria importar meu arquivo.

Main é apenas uma função criada, não tem a função que main tem no java, não é necessário. É apenas uma boa prática, para mostrar o ponto de entrada/começo do meu programa.

## interpolar = inserir, ao trocar algo por isso






---
### Fontes
Treina Recife - Portal do Aluno
