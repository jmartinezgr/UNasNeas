def obtener_numeros(limite, paso):
    if paso == 0:
        return set(range(1, limite + 1))
    else:
        arreglo = set()
        numero = 1+paso
        while numero <=limite:
            arreglo.add(numero)
            numero += 1+paso
        return arreglo

for _ in range(int(input())):
    r, v, a, n = map(int, input().split())
    conjunto_n = obtener_numeros(n, r) | obtener_numeros(n, v) | obtener_numeros(n, a)
    print(len(conjunto_n))