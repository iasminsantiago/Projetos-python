# Objetivo: Determinar se ano informado é bissexto ou não
		# Ano bissexto:
			# Tem 366 dias, assim calendário anual é alinhado a translação e estações da Terra;
			# Logo, anos com 29 dias em fevereiro são bissextos;
		    # divisível por 400  ou  divisível por 4 mas não por 100.


def verificador_ano_bissexto():
    ano=(int(input("Informe ano: ")))

# Verificar se ano é bissexto usando condições:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano != 100 == 0):
        print("SIM")
    else:
        print("NÃO")


# chamar a função explicitamente, assim ela será executada. 
# Quando usamos def, apenas criamos o bloco de código que será executado quando essa função for chamada. 
# A função não é executada automaticamente ao ser definida no def.
verificador_ano_bissexto()

# Se não coloca a chamada da função verificador_ano_bissexto() no final, o Python nunca executará seu código.