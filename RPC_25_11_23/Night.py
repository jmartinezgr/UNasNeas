velitas = int(input())
tri = 3
aux = 3
cont=0
while velitas >= 3:
    if velitas < tri:
        tri,aux = 3,3
    else:
        velitas -= tri
        tri += aux
        aux+= 1
        cont+=1
print(cont,velitas)