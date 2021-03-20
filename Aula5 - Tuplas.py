#listas e tuplas

lista = [1,2,3,4,5,6,7,8,9,10]

lista_animal = ['gato','cachorro','jacare','macaco']

for contaLista in lista:
    print(lista_animal, lista)
    print(len(lista)) #aqui soma a lista
    print('minimo', min(lista)) #valor minimo da lista
    print(str(lista))

    if 'Curuja' in lista_animal:
        print('Existe um ', str(lista_animal), 'na lista')
        print('esta na posição ', len(lista_animal[3]))

    else:
        print('nao existe esse animal na lista deseja incluir ?')
        teclado = str(input())
        lista_animal.append(teclado)
        print(lista_animal)
