#  Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
p = float(input('Primeira nota do aluno: '))
s = float(input('Segunda nota do aluno: '))
média = (p + s)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(p, s, média))

# Atenção: : '     (.+.)/2 checar equações. Um programa só é um programa quando ele resolve um problema.
#  :.1f = após o ponto flutuante, coloque apenas 1 dígito. Python fará pra mim o arredondamento algébrico