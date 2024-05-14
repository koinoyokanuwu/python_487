'''Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y
el área (pi*r)^2 del círculo inscrito.'''

def longitud_circunferencia(radio):
    # Longitud de la circunferencia
    longitud = 2 * 3.1416 * radio
    return longitud

def area_circulo_inscrito(radio):
    # Área del círculo inscrito
    area = 3.1416 * (radio**2)
    return area

# Leer el radio de la circunferencia desde el usuario
radio_circunferencia = float(input("Ingresa el radio de la circunferencia: "))

# Calcular la longitud de la circunferencia
longitud = longitud_circunferencia(radio_circunferencia)

# Calcular el área del círculo inscrito
area_inscrito = area_circulo_inscrito(radio_circunferencia)

# Mostrar resultados
print("La longitud de la circunferencia es:", longitud)
print("El área del círculo inscrito es:", area_inscrito)