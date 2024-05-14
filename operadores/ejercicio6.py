#Escribir un algoritmo que determine el área y el volúmen de un cilindro.
def area_cilindro(radio, altura):
    # Área de la base del cilindro
    area_base = 3.1416 * radio**2
    # Área lateral del cilindro
    area_lateral = 2 * 3.1416 * radio * altura
    # Área total del cilindro
    area_total = 2 * area_base + area_lateral
    return area_total

def volumen_cilindro(radio, altura):
    # Volumen del cilindro
    volumen = 3.1416 * radio**2 * altura
    return volumen

# Datos del cilindro
radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))

# Calcular área y volumen
area = area_cilindro(radio, altura)
volumen = volumen_cilindro(radio, altura)

# Mostrar resultados
print("El área del cilindro es:", area)
print("El volumen del cilindro es:", volumen)