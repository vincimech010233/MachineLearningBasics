import numpy as np

# Definición del espacio 2D y el objetivo
num_estados = 16  # Espacio 2D de 4x4 = 16 estados
num_acciones = 4  # 4 acciones posibles: arriba, abajo, izquierda, derecha

# Parámetros de Q-learning
Q = np.zeros((num_estados, num_acciones))  # Tabla Q inicializada en ceros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Exploración epsilon-greedy

# Definición del objetivo
objetivo = 15

# Función para tomar una acción basada en epsilon-greedy
def tomar_accion(estado):
    if np.random.rand() < epsilon:
        return np.random.choice(num_acciones)  # Exploración aleatoria
    else:
        return np.argmax(Q[estado, :])  # Explotación basada en Q

# Entrenamiento del agente
num_episodios = 1000

for episodio in range(num_episodios):
    estado_actual = 0  # Iniciar en el estado 0 (esquina superior izquierda)
    juego_en_curso = True

    while juego_en_curso:
        accion = tomar_accion(estado_actual)
        
        # Simular el movimiento y obtener la recompensa
        if accion == 0:  # Arriba
            nuevo_estado = max(estado_actual - 4, 0)
        elif accion == 1:  # Abajo
            nuevo_estado = min(estado_actual + 4, num_estados - 1)
        elif accion == 2:  # Izquierda
            nuevo_estado = max(estado_actual - 1, 0)
        else:  # Derecha
            nuevo_estado = min(estado_actual + 1, num_estados - 1)
        
        # Definir una recompensa simple (1 si llega al objetivo, 0 en otros casos)
        recompensa = 1 if nuevo_estado == objetivo else 0

        # Actualizar la tabla Q usando la ecuación Q-learning
        Q[estado_actual, accion] += alpha * (recompensa + gamma * np.max(Q[nuevo_estado, :]) - Q[estado_actual, accion])

        estado_actual = nuevo_estado

        if estado_actual == objetivo:
            juego_en_curso = False

# Función para que el agente navegue en el espacio
def navegar_agente():
    estado_actual = 0
    while estado_actual != objetivo:
        print("Estado actual:", estado_actual)
        accion = tomar_accion(estado_actual)

        # Simular el movimiento
        if accion == 0:  # Arriba
            nuevo_estado = max(estado_actual - 4, 0)
        elif accion == 1:  # Abajo
            nuevo_estado = min(estado_actual + 4, num_estados - 1)
        elif accion == 2:  # Izquierda
            nuevo_estado = max(estado_actual - 1, 0)
        else:  # Derecha
            nuevo_estado = min(estado_actual + 1, num_estados - 1)

        estado_actual = nuevo_estado

    print("¡Objetivo alcanzado en el estado", estado_actual, "!")

# Ejecutar la navegación del agente entrenado
navegar_agente()
