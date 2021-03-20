
entradaTeclado = int(input("Entre com um valor \n"))

for num in range(entradaTeclado + 1):               #conta de zero a cem
    divisao = 0
    for cont in range(1, num + 1):   #contador aninhado
        restoDivisao = num % cont    #resto
        if restoDivisao == 0:
            divisao += 1
    if divisao == 2:
                print(num)          #imprime apenas os numeros primos