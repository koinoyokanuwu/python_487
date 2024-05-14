'''Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el
menor.'''

# Solicitar al usuario los datos
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Comparar los números para encontrar el mayor y el menor
if num1 > num2:
    mayor = num1
    menor = num2
elif num1 < num2:
    mayor = num2
    menor = num1
else:
    print("Los números son iguales.")
    # Salir del programa si los números son iguales
    exit()

# Mostrar el resultado
print("El mayor número es:", mayor)
print("El menor número es:", menor)