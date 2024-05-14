'''Escriba un programa que lea tres números enteros positivos y que calcule e imprima en
pantalla el menor y el mayor de ellos'''

#Solicitar los datos al usuario
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))
num3 = int(input("Ingrese el tercer número entero positivo: "))

# Verificar si los números son positivos
if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("Por favor, ingrese solo números enteros positivos.")
    exit()

# Inicializar variables para almacenar el menor y el mayor número
menor = num1
mayor = num1

# Comparar cada número con el menor y el mayor actual
if num2 < menor:
    menor = num2
elif num2 > mayor:
    mayor = num2

if num3 < menor:
    menor = num3
elif num3 > mayor:
    mayor = num3

# Imprimir el menor y el mayor número
print("El menor número es:", menor)
print("El mayor número es:", mayor)