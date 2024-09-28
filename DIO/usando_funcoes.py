def exibir_poema(data_extenso, *lista, **dicionario): 
# o primeiro argumento será data_extenso
# args é separação por vírgula. 
# Quando acabar os valores separados por , ele entenderá que começa os kwargs/dicionários; 
	
		# o que esse método fará:	
		texto = "\n".join(lista) # pulará linha em cada arg. de lista
		meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
		mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
		print(mensagem)
		
		
		

# chamando a função para ser exibida:		
exibir_poema("Sexta-feira, 26 de Agosto de 2024", "Zen of Python", "Beautiful is better than ugly.", autor = "Tim Peters", ano=1999)
# data_extenso será a primeira informação
# args é "Zen of Python", "Beautiful is better than ugly." pois são separados por ,
# kwargs é autor = "Tim Peters", ano=1999 por ter pares chave=valor