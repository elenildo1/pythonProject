#Variaveis

a = float(input("Entre com o primeiro numero :"))
b = float(input("Entre com o segundo numero :"))

soma = a + b #soma
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto  = a % b #resto

print("A soma de ", a, " + ", b," = " , soma)
print("A subtracao de ", a, "-",  b, "=" , subtracao)
print("A Divisão de", a, "/ por ", b , " = ", divisao)
print("O resto de ", a, " / ", b , resto)
#print(type(soma))

print("Outra forma de imprimir :")


e = 10 / 2
d = 10 % 2
print(e)


print('soma:{sm}'.format(sm = soma).format(subtracao))


