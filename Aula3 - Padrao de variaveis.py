a = int(input("Primeiro valor : \n "))
b = int(input("segundo valor : \n "))
c = int(input("terceiro numero: \n"))
resto = a % b

if a > b:
    print(format(a))

elif b > a and b < c:
    print(format(c))
else:
    print(format(b))

if resto == 0:
    print("Foi digitado apenas numeros pares = ", resto)