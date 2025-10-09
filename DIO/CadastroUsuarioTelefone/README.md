# 📱 Projeto: Cadastro de Usuário de Telefone

Este projeto foi desenvolvido como um desafio de Python para praticar **Programação Orientada a Objetos (POO)** e **encapsulamento**.  
O programa permite criar um usuário de telefone com nome, número e plano associado, simulando três tipos de planos:

- Plano Essencial Fibra  
- Plano Prata Fibra  
- Plano Premium Fibra  

---

## 🧩 Funcionalidade

1. Solicita ao usuário o **nome**, **número de telefone** e **plano**.  
2. Cria um objeto da classe `UsuarioTelefone` com esses dados.  
3. Retorna uma mensagem indicando que o usuário foi criado com sucesso.

---

## 🧪 Exemplos de execução

**Entrada:**
Ana
(11) 91111-1111
Plano Essencial Fibra


**Saída:**


Usuário Ana criado com sucesso.


**Entrada:**


Sofia
(22) 92222-2222
Plano Prata Fibra


**Saída:**


Usuário Sofia criado com sucesso.


---

## 🧠 Conceitos Aplicados

- **Classe**: `UsuarioTelefone` representa um usuário de telefone.  
- **Encapsulamento**: os atributos `nome`, `numero` e `plano` são privados (`__atributo`).  
- **Método construtor**: `__init__` inicializa os atributos do objeto.  
- **Método especial `__str__`**: define a representação em string do objeto.  
- **Getter (`@property`)**: permite acessar atributos privados de forma segura.

---

## 📝 Observações

- O código pode ser expandido para **validar o número de telefone** ou **verificar planos disponíveis**.  
- Ideal para estudos de **POO** e **Python básico a intermediário**.
