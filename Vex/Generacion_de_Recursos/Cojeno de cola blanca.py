import random
import math

# Definir parámetros iniciales crianza
tiempo_simulacion = 6  # Meses a simular
poblacion_inicial_adulta = 1  # Contando por parejas
poblacion_inicial_infantil = 0  # Contado por parejas
madurez_sexual_meses = 5  # Meses para alcanzar la madurez sexual
crecimiento_poblacional_adulto = [poblacion_inicial_adulta]  # Almacenar el crecimiento adulto en cada mes
crecimiento_poblacional_infantil = [poblacion_inicial_infantil]  # Almacenar el crecimiento infantil en cada mes

# Definir parámetros iniciales matanza
poblacion_reserva = 0.9  # Reservamos para continuar la crianza un 10% de la población adulta
carne_acumulada = []
piel_acumulada = []

# Calcular crecimiento
for mes in range(1, int(tiempo_simulacion) + 1):
    crias_por_camada = (random.randint(1, 14))

    # Cada pareja adulta produce crías_por_camada / 2 parejas nuevas cada mes | redondeado a numeros enteros al alza.
    nuevas_parejas = math.ceil(crecimiento_poblacional_adulto[-1] * (crias_por_camada / 2))

    if mes < 5:
        crecimiento_poblacional_infantil.append(nuevas_parejas)
    else:
        crecimiento_poblacional_infantil.append(nuevas_parejas)
        # del crecimiento_poblacional_infantil[-6]
        poblacion_actual = crecimiento_poblacional_adulto[-1] + crecimiento_poblacional_infantil[-5]
        crecimiento_poblacional_adulto.append(poblacion_actual)

# Simular matanza actual
for conejo in range(1, int(2*(poblacion_reserva * crecimiento_poblacional_adulto[-1])) + 1):  # Son parejas
    rendimiento_carne = random.randint(2, 5)
    carne_acumulada.append(rendimiento_carne)

    rendimiento_piel = random.randint(1, 2)
    piel_acumulada.append(rendimiento_piel)

# Mostrar resutlados crianza
print("Adultos totales: " + str(2 * crecimiento_poblacional_adulto[-1]))
print("Infantes totales: " + str(sum(2 * crecimiento_poblacional_infantil[-5:])))  # Muestra los últimos 5 y los suma
print("     Infantes de 1 mes: " + str(2 * crecimiento_poblacional_infantil[-5]))
print("     Infantes de 2 mes: " + str(2 * crecimiento_poblacional_infantil[-4]))
print("     Infantes de 3 mes: " + str(2 * crecimiento_poblacional_infantil[-3]))
print("     Infantes de 4 mes: " + str(2 * crecimiento_poblacional_infantil[-2]))
print("     Infantes de 5 mes: " + str(2 * crecimiento_poblacional_infantil[-1]))


# Mostrar resutlados matanza
print("Carne acumulada: " + str(sum(carne_acumulada)) + " Kg")
print("Piel acumulada: " + str(sum(piel_acumulada)) + " Kg")
