#Este algoritmo calcula el factorial de un número ingresado 
# por el usuario utilizando un bucle while.

n = int(input("Ingrese un número: "))
factorial = 1
i = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print("El factorial de", n, "es", factorial)
