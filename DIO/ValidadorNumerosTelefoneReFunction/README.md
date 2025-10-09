# 💻 Projeto: Validador de Número de Telefone

Este projeto foi desenvolvido como um desafio de Python para **praticar expressões regulares (regex)**.  
O programa permite que o usuário **verifique se um número de telefone está no formato correto**.

---

## 🧩 Funcionalidade

- O formato aceito para números de telefone é: `(XX) 9XXXX-XXXX`  
  Onde `X` representa um dígito de 0 a 9.  
- O programa retorna uma mensagem indicando se o número é **válido** ou **inválido**.

---

## 🧪 Exemplos de Execução

**Entrada:**
(88) 98888-8888

**Saída:**


Número de telefone válido.


**Entrada:**


(11)91111-1111

**Saída:**


Número de telefone inválido.


**Entrada:**


225555-555

**Saída:**


Número de telefone inválido.


---

## 🧠 Como Funciona o Código

- Usa-se o módulo `re` do Python para trabalhar com **expressões regulares**.  
- A função `validate_numero_telefone()` define um **padrão regex** para validar o formato do telefone.  
- `re.match()` verifica se o número fornecido corresponde ao padrão.  
- O programa retorna `"Número de telefone válido."` ou `"Número de telefone inválido."`.

---

## 📝 Observações

- `r'^\(\d{2}\) 9\d{4}-\d{4}$'` → regex para garantir que o telefone está exatamente no formato correto.  
- Pode ser facilmente adaptado para validar outros formatos de telefone.

---

## 🧾 Autor(a)

Projeto desenvolvido por **Iasmin S.** como parte dos estudos em **Python** e **expressões regulares** 🩷
