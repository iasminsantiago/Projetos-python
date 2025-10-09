# Validador de Número de Telefone
# Este script verifica se um número de telefone fornecido pelo usuário
# está no formato: (XX) 9XXXX-XXXX, onde X é um dígito de 0 a 9.

import re  # Importa o módulo de expressões regulares

def validate_numero_telefone(phone_number):
    """
    Valida se o número de telefone está no formato: (XX) 9XXXX-XXXX
    Onde X é um dígito de 0 a 9 e o espaço entre o DDD e o número é obrigatório.
    """
    # Define o padrão de expressão regular
    pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    # ^ → início da string, $ → fim da string
    # \d{2} → dois dígitos para o DDD
    # 9\d{4}-\d{4} → número de telefone no formato 9XXXX-XXXX

    # Verifica se o número corresponde ao padrão
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone
phone_number = input("Digite o número de telefone: ")

# Chama a função e armazena o resultado
result = validate_numero_telefone(phone_number)

# Imprime o resultado
print(result)
