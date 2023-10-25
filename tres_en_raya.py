import numpy as np

# Definición del tablero de tres en raya
tablero = np.zeros((3, 3))  # 0: casilla vacía, 1: jugador X, -1: jugador O

# Parámetros de Q-learning
num_estados = 3 ** 9  # 3^9 posibles combinaciones de estado del tablero (cada casilla puede estar vacía, X o O)
num_acciones = 9  # 9 posiciones en el tablero
Q = np.zeros((num_estados, num_acciones))  # Tabla Q inicializada en ceros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Exploración epsilon-greedy

# Función para codificar el estado del tablero en un número único
def codificar_estado(tablero):
    estado = 0
    for i in range(3):
        for j in range(3):
            estado = estado * 3 + tablero[i, j] + 1
    return estado

# Función para obtener las acciones válidas (casillas vacías) desde un estado
def acciones_validas(tablero):
    acciones = []
    for i in range(3):
        for j in range(3):
            if tablero[i, j] == 0:
                acciones.append(3 * i + j)
    return acciones

# Función para verificar si el juego ha terminado y quién ha ganado
def juego_terminado(tablero):
    for i in range(3):
        if np.all(tablero[i, :] == 1) or np.all(tablero[i, :] == -1):
            return True, tablero[i, 0]
        if np.all(tablero[:, i] == 1) or np.all(tablero[:, i] == -1):
            return True, tablero[0, i]
    if np.all(np.diag(tablero) == 1) or np.all(np.diag(tablero) == -1) or np.all(np.diag(np.fliplr(tablero)) == 1) or np.all(np.diag(np.fliplr(tablero)) == -1):
        return True, tablero[1, 1]
    if not 0 in tablero:
        return True, 0  # Empate
    return False, None

# Algoritmo Q-learning
num_episodios = 10000

for episodio in range(num_episodios):
    tablero_actual = np.zeros((3, 3))
    estado_actual = codificar_estado(tablero_actual)
    juego_en_curso = True

    while juego_en_curso:
        if np.random.rand() < epsilon:
            # Acción aleatoria (exploración)
            acciones = acciones_validas(tablero_actual)
            accion = np.random.choice(acciones)
        else:
            # Acción basada en la tabla Q (explotación)
            accion = np.argmax(Q[int(estado_actual)])
        
        fila = accion // 3
        columna = accion % 3
        tablero_actual[fila, columna] = 1  # Jugador X realiza la acción
        
        juego_en_curso, ganador = juego_terminado(tablero_actual)
        if juego_en_curso:
            # Turno del jugador O (oponente aleatorio)
            acciones = acciones_validas(tablero_actual)
            accion_oponente = np.random.choice(acciones)
            fila_oponente = accion_oponente // 3
            columna_oponente = accion_oponente % 3
            tablero_actual[fila_oponente, columna_oponente] = -1

        siguiente_estado = codificar_estado(tablero_actual)
        recompensa = 0

        if not juego_en_curso:
            if ganador == 1:
                recompensa = 1  # Jugador X gana
            elif ganador == -1:
                recompensa = -1  # Jugador O gana
        
        Q[int(estado_actual), int(accion)] += alpha * (recompensa + gamma * np.max(Q[int(siguiente_estado)]) - Q[int(estado_actual), int(accion)])
        estado_actual = siguiente_estado

# Función para jugar contra el agente entrenado
def jugar_contra_agente():
    tablero_actual = np.zeros((3, 3))
    juego_en_curso = True

    while juego_en_curso:
        print(tablero_actual)
        acciones = acciones_validas(tablero_actual)
        if acciones:
            accion = input("Ingresa tu movimiento (0-8): ")
            try:
                accion = int(accion)
                if accion in acciones:
                    fila = accion // 3
                    columna = accion % 3
                    tablero_actual[fila, columna] = -1
                else:
                    print("Movimiento no válido. Intenta de nuevo.")
                    continue
            except ValueError:
                print("Entrada no válida. Ingresa un número entre 0 y 8.")
                continue
        
        juego_en_curso, ganador = juego_terminado(tablero_actual)  # Verificar si el juego ha terminado después del movimiento del jugador

        if juego_en_curso:
            acciones = acciones_validas(tablero_actual)
            if acciones:
                estado_actual = codificar_estado(tablero_actual)
                accion = np.argmax(Q[int(estado_actual)])  # Usar Q para la siguiente acción
                fila = accion // 3
                columna = accion % 3
                tablero_actual[fila, columna] = 1
            else:
                print("Empate.")
                break

        estado_actual = codificar_estado(tablero_actual)  # Actualizar el estado actual

    if ganador == 1:
        print("¡Has ganado!")
    elif ganador == -1:
        print("El agente ha ganado.")
    else:
        print("Empate.")

# Jugar contra el agente entrenado
jugar_contra_agente()
