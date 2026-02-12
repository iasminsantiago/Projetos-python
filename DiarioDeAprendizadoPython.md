## DIFERENÇAS
- snake_case
- Tem PIP
- não finaliza com ;
- não tem main padrão, este é só uma boa prática

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


## interpolar 
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



---
### Fontes
Treina Recife - Portal do Aluno
