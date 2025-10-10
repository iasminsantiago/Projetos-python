# Projeto Telefone

# 1. Este projeto é uma sequência de exercícios em Python para gerenciar usuários de telefone, planos e realizar chamadas. Ele utiliza conceitos de **Programação Orientada a Objetos (POO)**, **encapsulamento**, **herança** e manipulação de atributos e métodos.

---

## Exercício 1 - Criar Usuário de Telefone

Arquivo: `01_usuario_telefone.py`

Funcionalidade:
- Cria uma classe `UsuarioTelefone` com os atributos: `nome`, `numero` e `plano`.
- Permite criar um usuário e imprimir uma mensagem de sucesso.
- Utiliza encapsulamento para proteger os atributos da classe.

Entrada:
- Nome do usuário
- Número de telefone
- Plano

Saída:
- Mensagem indicando que o usuário foi criado com sucesso.

---

## Exercício 2 - Verificar Saldo do Plano

Arquivo: `02_verificar_saldo.py`

Funcionalidade:
- Cria uma classe `PlanoTelefone` com os atributos `nome` e `saldo`.
- Método `verificar_saldo` para checar o saldo atual do plano.
- Método `mensagem_personalizada` para retornar uma mensagem baseada no saldo:
  - Saldo < 10: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
  - Saldo >= 50: "Parabéns! Continue aproveitando seu plano sem preocupações."
  - Caso contrário: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
- A classe `UsuarioTelefone` utiliza `PlanoTelefone` para associar um plano ao usuário.

Entrada:
- Nome do usuário
- Plano (Essencial, Prata, Premium)
- Saldo inicial

Saída:
- Mensagem personalizada de acordo com o saldo.

---

## Exercício 3 - Fazer Chamada

Arquivo: `03_fazer_chamada.py`

Funcionalidade:
- Permite que o usuário realize chamadas para outros números.
- Cada chamada tem custo de $0.10 por minuto.
- Deduz automaticamente o valor da chamada do saldo do plano.
- Retorna mensagem de sucesso ou alerta de saldo insuficiente.

Entrada:
- Nome do usuário
- Número do usuário
- Saldo inicial
- Número do destino



# 2. Execute o arquivo desejado:

python 01_usuario_telefone.py
python 02_verificar_saldo.py
python 03_fazer_chamada.py


# 3. Siga as instruções de entrada solicitadas no terminal.
