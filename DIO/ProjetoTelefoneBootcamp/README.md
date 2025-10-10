# 📱 Projeto: Sistema de Usuário e Plano Telefônico

Este projeto em Python foi desenvolvido como exercício de aprendizado sobre **Programação Orientada a Objetos (POO)**, encapsulamento, herança e manipulação de objetos. Ele consiste em três exercícios principais, cada um com funcionalidades diferentes relacionadas a **usuários de telefone e seus planos**.

---

## 1️⃣ Exercício 1 – Criando Usuário de Telefone

### 🎯 Objetivo
Criar uma classe `UsuarioTelefone` que representa um usuário de telefone com atributos **nome**, **número** e **plano**.

### 📚 Conceitos utilizados
- **Classe e objeto**: A classe `UsuarioTelefone` define a estrutura do usuário.  
- **Construtor (`__init__`)**: Inicializa os atributos do objeto.  
- **Encapsulamento**: Protegemos os atributos privados usando `self.nome`, `self.numero` e `self.plano`.  
- **Método especial (`__str__`)**: Retorna uma mensagem de sucesso quando o usuário é criado.  

### 💻 Código principal
usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)
✅ O programa solicita:
Nome do usuário
Número do telefone
Plano (Essencial, Prata, Premium)

💬 E retorna:
Usuário <nome> criado com sucesso.
Aprendizado:
Entendi como criar uma classe básica em Python e como inicializar objetos com dados do usuário, algo semelhante ao que fazemos em Java usando construtores. ✨

## 2️⃣ Exercício 2 – Verificando o Saldo do Plano
🎯 Objetivo
Adicionar uma classe PlanoTelefone e relacionar cada usuário a um plano, permitindo verificar o saldo e gerar mensagens personalizadas.

📚 Conceitos utilizados
Composição: A classe UsuarioTelefone contém um objeto PlanoTelefone.
Encapsulamento de atributos: __saldo é privado e só pode ser acessado via métodos.
Métodos personalizados: verificar_saldo() retorna o saldo, e mensagem_personalizada() cria mensagens diferentes dependendo do valor do saldo.

💻 Código principal
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
💡 O programa verifica:

Saldo < 10 → "Seu saldo está baixo..." ⚠️
Saldo >= 50 → "Parabéns! Continue aproveitando..." 🎉
Caso contrário → "Saldo razoável..." 👍

Aprendizado:
Comecei a ver composição de objetos (uma classe dentro de outra) e como criar métodos que retornam informações sem expor os atributos privados. É equivalente a usar private e getters em Java. 🛡️

## 3️⃣ Exercício 3 – Fazendo Chamadas
🎯 Objetivo
Criar funcionalidades para que um usuário faça chamadas para outro usuário, com cálculo de custo e dedução de saldo.

📚 Conceitos utilizados
Herança: UsuarioPrePago herda de UsuarioTelefone e adiciona comportamento específico para usuários pré-pagos.
Encapsulamento: __saldo continua privado, modificado apenas por métodos específicos.
Cálculo de custo: Cada minuto de chamada custa $0.10, e o custo é deduzido do saldo do usuário.
Verificação de saldo: Antes de fazer a chamada, o programa verifica se o usuário tem saldo suficiente.

💻 Código principal
usuario_pre_pago.fazer_chamada(destinatario, duracao)
📋 O programa:
Recebe informações do usuário: nome, número, saldo inicial.
Recebe informações da chamada: destinatário e duração.
Calcula o custo e deduz do saldo, se possível.
Retorna mensagem de sucesso ou saldo insuficiente.

Aprendizado:
Aqui eu vi herança na prática e como métodos podem interagir com outros objetos (plano). É equivalente a ter uma classe User e uma classe Plan em Java, e o usuário chama métodos do plano sem acessar os atributos privados diretamente. 🔄

## 🧠 Conceitos gerais aprendidos
Python POO vs Java:

Em Java: usamos private, getters/setters, e construtores.

Em Python: usamos __atributo para encapsulamento, @property para getters, e __init__ como construtor.

Composição: Um objeto pode ter outro objeto como atributo.
Herança: Uma subclasse pode herdar atributos e métodos de uma superclasse.
Encapsulamento: Proteger atributos com __ e criar métodos para manipulação segura.
Métodos especiais: __init__, __str__ ajudam na criação e exibição de objetos.
Interação com o usuário: Uso de input() para capturar dados e print() para exibir resultados.

Cálculos e lógica condicional: if, elif, else e cálculos dentro de métodos.

## 🗂 Estrutura da pasta do projeto
projeto_telefone/
│
├── 01_usuario_telefone.py
├── 02_verificar_saldo.py
├── 03_fazer_chamada.py
└── README.md
Cada exercício tem seu próprio arquivo .py, mas todos estão relacionados ao mesmo conceito de usuário de telefone e plano. 📁

💡 Dicas para estudo futuro
Revisar como objetos interagem entre si (usuário → plano).
Comparar os conceitos de Java POO que você já conhece com a sintaxe Python.
Rever encapsulamento e métodos especiais (__init__, __str__) para entender melhor como Python organiza a POO.
Testar diferentes cenários de saldo e chamadas para ver o comportamento do sistema. 🔍
