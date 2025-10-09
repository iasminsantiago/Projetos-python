# 💻 Projeto: Recomendador de Plano de Internet

Este projeto foi desenvolvido como parte de um desafio de **Python básico**, com o objetivo de ajudar clientes de uma empresa de telecomunicações a **descobrir o plano de internet ideal** de acordo com seu consumo médio mensal de dados.

---

## 🧠 Lógica do Desafio

O programa solicita ao usuário que informe o consumo médio mensal (em GB) e, com base nesse valor, recomenda um dos três planos disponíveis:

| Faixa de Consumo | Plano Recomendado |
|------------------|-------------------|
| Até **10 GB** | Plano Essencial Fibra - 50Mbps |
| Acima de **10 GB até 20 GB** | Plano Prata Fibra - 100Mbps |
| Acima de **20 GB** | Plano Premium Fibra - 300Mbps |

---

## 🧩 Estrutura do Código

```python
# Cria uma função que recebe o consumo médio mensal
def recomendar_plano(consumo):
    # Verifica a faixa de consumo informada
    if consumo <= 10:
        # Retorna o plano Essencial para quem consome até 10 GB
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        # Retorna o plano Prata para consumo entre 10 e 20 GB
        return "Plano Prata Fibra - 100Mbps"
    else:
        # Retorna o plano Premium para consumo acima de 20 GB
        return "Plano Premium Fibra - 300Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados (em GB)
consumo = float(input("Informe seu consumo médio mensal (em GB): "))

# Chama a função e exibe o plano recomendado
print(recomendar_plano(consumo))
