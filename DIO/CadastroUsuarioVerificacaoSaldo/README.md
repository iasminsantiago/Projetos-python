# 📱 Projeto: Usuário de Telefone com Verificação de Saldo

Este projeto foi desenvolvido como um desafio de Python para praticar **Programação Orientada a Objetos (POO)**, **encapsulamento** e **interação entre classes**.  
O programa permite criar um usuário de telefone e associar um plano, que possui um saldo. É possível verificar o saldo do plano e gerar uma mensagem personalizada de acordo com o valor disponível.

---

## 🧩 Funcionalidade

1. Solicita ao usuário o **nome**, **plano** e **saldo inicial**.  
2. Cria um objeto da classe `PlanoTelefone` com nome e saldo.  
3. Cria um objeto da classe `UsuarioTelefone` associando o plano ao usuário.  
4. Retorna uma mensagem personalizada de acordo com o saldo do usuário.

---

## 🧪 Condições da verificação do saldo

- Caso o saldo seja menor que 10:  
  `"Seu saldo está baixo. Recarregue e use os serviços do seu plano."`  
- Caso o saldo seja maior ou igual a 50:  
  `"Parabéns! Continue aproveitando seu plano sem preocupações."`  
- Caso contrário:  
  `"Seu saldo está razoável. Aproveite o uso moderado do seu plano."`

---

## 🧪 Exemplos de execução

**Entrada:**
João
Essencial
9


**Saída:**


Seu saldo está baixo. Recarregue e use os serviços do seu plano.


**Entrada:**


Catarina
Premium
50


**Saída:**


Parabéns! Continue aproveitando seu plano sem preocupações.


---

## 🧠 Conceitos Aplicados

- **Classe**: `PlanoTelefone` e `UsuarioTelefone`.  
- **Encapsulamento**: atributos privados `__nome` e `__saldo` no plano.  
- **Método construtor**: `__init__` inicializa os atributos do objeto.  
- **Métodos**: `verificar_saldo()` e `mensagem_personalizada()` no plano; `verificar_saldo()` no usuário.  
- **Interação entre classes**: `UsuarioTelefone` utiliza métodos do objeto `PlanoTelefone`.

---

## 📝 Observações

- O código pode ser expandido para **validar o número de telefone** ou **verificar tipos de plano válidos**.  
- Ideal para estudos de **POO**, **encapsulamento** e **Python intermediário**.
