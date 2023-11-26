def obtener_numeros(n):
    limite = (n - 1) // 2
    numeros = [2 * i + 1 for i in range(limite + 1)]
    return numeros

# Ejemplo
n = 10
resultado = obtener_numeros(n)
print(resultado)