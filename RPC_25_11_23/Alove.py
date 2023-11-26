lista = input().split()
listmax = []
listmax.append(lista[0]+lista[1]+lista[2])
listmax.append(lista[0]+lista[2]+lista[1])
listmax.append(lista[1]+lista[0]+lista[2])
listmax.append(lista[1]+lista[2]+lista[0])
listmax.append(lista[2]+lista[1]+lista[0])
listmax.append(lista[2]+lista[0]+lista[1])
print(max(listmax, key=int))