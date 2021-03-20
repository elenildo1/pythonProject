#Exercicios bimestre

notaAprovado = 50
notaReprovado = 49
mensagemAprovado = "Parabéns voçê foi aprovado!!!"
mensagemReprovado = "Voçê não foi aprovado, se dedique um pouco mais ano que vem!!!!"

nomeAluno = str(input("Nome do Aluno ? \n"))

#Nota do primeiro bimestre
nota1 = float(input("Lançe a nota do 1º Bimestre \n"))
while nota1 > 100:
    nota1 = float(input("Lance  a nota do 1º Bimestre corretamente \n"))

#Nota do segundo bimestre
nota2 = float(input("Lance  a nota do 2º Bimestre \n"))
while nota2 > 100:
    nota2 = float(input("Lance  a nota do 2º Bimestre, corretamente \n"))

# Nota do terceiro bimestre
nota3 = float(input("Lance a nota do 3º Bimestre \n"))
while nota3 > 100:
    nota3 = float(input("Lance  a nota do 3º Bimestre, corretamente \n"))

#Nota do quarto bimestre
nota4 = float(input("Lance a nota do 4º Bimestre \n"))
while nota4 > 100:
    nota4 = float(input("Lance  a nota do 4º Bimestre, corretamente \n"))

#soma de todas as notas
somaNotas = (nota1 + nota2 + nota3 + nota4) / 4

if somaNotas > notaReprovado:
    print('{}'.format(somaNotas))
    print(nomeAluno, "\n", mensagemAprovado)
else:
    print('somaNotas:{resultado}'.format(resultado=somaNotas))
    print(nomeAluno, ", ", mensagemReprovado)

