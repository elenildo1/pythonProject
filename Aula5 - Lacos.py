# Exercicios para saber se um numero é primo

num = int(input("Entre com um numero qualquer\n"))
div = 0
for contador in range(1, num+1):
    resto = num % contador
    print(num, "dividido por ", contador, ' = ', resto)
    if resto == 0:
        div = div + 1

        print(resto)
if div == 2:
    print('numero {} é primo '.format(num))

else:
    print('numero {} nao e primo'.format(num))
