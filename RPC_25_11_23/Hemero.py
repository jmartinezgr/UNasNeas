entrada = list(map(int, input().split()))
n_meses = entrada[0]
cantidad_meses = entrada[1:]
dias_por_año = sum(cantidad_meses)
dias = 0
# Lectura rápida de fechas
fecha0 = list(map(int, input().split()))
fecha1 = list(map(int, input().split()))
dias += (fecha1[2] - fecha0[2]) * dias_por_año
if fecha0[1] != fecha1[1]:
    dias+= cantidad_meses[fecha0[1]-1]-fecha0[0]
    dias+= sum(cantidad_meses[fecha0[1]:fecha1[1]-1])
    dias+= fecha1[0]
else:
    dias+=fecha1[0]-fecha0[0]   

print(dias)