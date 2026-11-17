
import random
import time

PI_REAL = 3.14159


# ALGORITMO MONTE CARLO
def monte_carlo(N):
    puntos_dentro = 0

    inicio = time.perf_counter()

    for contador in range(N):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        if x**2 + y**2 <= 0.25:
            puntos_dentro += 1

    pi_estimado = 4 * puntos_dentro / N

    fin = time.perf_counter()

    diferencia = abs(PI_REAL - pi_estimado)
    tiempo = fin - inicio

    return pi_estimado, diferencia, tiempo


# ALGORITMO LAS VEGAS
def las_vegas(K):
    puntos_dentro = 0
    total_puntos = 0

    inicio = time.perf_counter()

    while puntos_dentro < K:
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)

        total_puntos += 1

        if x**2 + y**2 <= 0.25:
            puntos_dentro += 1

    pi_estimado = 4 * puntos_dentro / total_puntos

    fin = time.perf_counter()

    diferencia = abs(PI_REAL - pi_estimado)
    tiempo = fin - inicio

    return pi_estimado, diferencia, tiempo, total_puntos


# COMPARACION DE AMBOS ALGORITMOS
valores = [1000, 10000, 100000, 500000]

print("=" * 75)
print("          COMPARACION MONTE CARLO VS LAS VEGAS")
print("=" * 75)

for cantidad in valores:

    # Ejecutar Monte Carlo
    pi_mc, error_mc, tiempo_mc = monte_carlo(cantidad)

    # Ejecutar Las Vegas
    pi_lv, error_lv, tiempo_lv, total_lv = las_vegas(cantidad)

    print("\nCANTIDAD:", cantidad)
    print("-" * 75)

    print("MONTE CARLO")
    print("PI estimado:", pi_mc)
    print("Diferencia:", error_mc)
    print("Tiempo:", tiempo_mc, "segundos")

    print("\nLAS VEGAS")
    print("PI estimado:", pi_lv)
    print("Diferencia:", error_lv)
    print("Tiempo:", tiempo_lv, "segundos")
    print("Total de puntos generados:", total_lv)

    print("\nRESULTADO DE LA COMPARACION")

    if error_mc < error_lv:
        print("Mayor precision: MONTE CARLO")
    elif error_lv < error_mc:
        print("Mayor precision: LAS VEGAS")
    else:
        print("Ambos tienen la misma precision")

    if tiempo_mc < tiempo_lv:
        print("Menor tiempo: MONTE CARLO")
    elif tiempo_lv < tiempo_mc:
        print("Menor tiempo: LAS VEGAS")
    else:
        print("Ambos tienen el mismo tiempo")

    print("=" * 75)