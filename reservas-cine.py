
# Nombre: Wendy Nayely Brito Paccha
# Objetivo del programa:
# Gestionar la reserva de asientos de una sala de cine de 3 filas × 4 columnas.
# - 0 = asiento libre
# - 1 = asiento reservado
# El usuario ingresa fila y columna, se marca el asiento y se muestra la sala completa.

# Paso 1: Crear la matriz de asientos (3 filas, 4 columnas) inicializada en 0

asientos = [
    [0, 0, 0, 0],   # Fila 0
    [0, 0, 0, 0],   # Fila 1
    [0, 0, 0, 0]    # Fila 2
]

# Paso 2: Solicitar datos al usuario con validación de rango

print(" SISTEMA DE RESERVA DE ASIENTOS DE CINE")

# Leer y validar fila
while True:
    fila = int(input("Ingrese fila (0 a 2): "))
    if 0 <= fila <= 2:
        break
    print("⚠️  Fila inválida. Intente nuevamente (0, 1 o 2).")

# Leer y validar columna
while True:
    columna = int(input("Ingrese columna (0 a 3): "))
    if 0 <= columna <= 3:
        break
    print("⚠️  Columna inválida. Intente nuevamente (0, 1, 2 o 3).")

# Paso 3: Verificar si el asiento ya está reservado y marcarlo

if asientos[fila][columna] == 1:
    print("ℹ️  Este asiento ya se encuentra reservado.")
else:
    asientos[fila][columna] = 1
    print("✅ Asiento reservado con éxito.")


# Paso 4: Mostrar el estado completo de la sala con bucles anidados

print("\n ESTADO ACTUAL DE LA SALA")
for i in range(3):               # Bucle exterior: recorre cada fila
    for j in range(4):           # Bucle interior: recorre cada columna de la fila
        print(asientos[i][j], end="  ")  # Imprime valor con espacio, sin salto de línea
    print()                      # Salto de línea al terminar cada fila
print()

