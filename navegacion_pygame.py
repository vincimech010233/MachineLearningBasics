import pygame
import numpy as np

# Dimensiones de la pantalla
ANCHO = 400
ALTO = 400

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Definición del espacio 2D y el objetivo
num_estados = 16
num_acciones = 4

# Parámetros de Q-learning
Q = np.zeros((num_estados, num_acciones))
#alpha = 0.1
#gamma = 0.9
#epsilon = 0.1
alpha = 1  # Tasa de aprendizaje más alta
epsilon = 0.05  # Menos exploración
gamma = 0.9

objetivo = 15

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Q-Learning 2D")

# Función para tomar una acción basada en epsilon-greedy
def tomar_accion(estado):
    if np.random.rand() < epsilon:
        return np.random.choice(num_acciones)
    else:
        return np.argmax(Q[estado, :])

# Función para dibujar el agente y el objetivo
def dibujar(estado):
    pantalla.fill(BLANCO)
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(pantalla, NEGRO, (i * 100, j * 100, 100, 100), 1)
    agente_x = estado % 4 * 100 + 50
    agente_y = estado // 4 * 100 + 50
    pygame.draw.circle(pantalla, VERDE, (agente_x, agente_y), 20)
    objetivo_x = objetivo % 4 * 100 + 50
    objetivo_y = objetivo // 4 * 100 + 50
    pygame.draw.circle(pantalla, NEGRO, (objetivo_x, objetivo_y), 20)
    pygame.display.flip()

# Entrenamiento del agente
num_episodios = 1000

for episodio in range(num_episodios):
    estado_actual = 0
    juego_en_curso = True

    while juego_en_curso:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        accion = tomar_accion(estado_actual)

        if accion == 0:  # Arriba
            nuevo_estado = max(estado_actual - 4, 0)
        elif accion == 1:  # Abajo
            nuevo_estado = min(estado_actual + 4, num_estados - 1)
        elif accion == 2:  # Izquierda
            nuevo_estado = max(estado_actual - 1, 0)
        else:  # Derecha
            nuevo_estado = min(estado_actual + 1, num_estados - 1)

        recompensa = 1 if nuevo_estado == objetivo else 0

        Q[estado_actual, accion] += alpha * (recompensa + gamma * np.max(Q[nuevo_estado, :]) - Q[estado_actual, accion])

        estado_actual = nuevo_estado

        if estado_actual == objetivo:
            juego_en_curso = False

        dibujar(estado_actual)

# Función para que el agente navegue en el espacio
def navegar_agente():
    estado_actual = 0
    while estado_actual != objetivo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        accion = tomar_accion(estado_actual)

        if accion == 0:  # Arriba
            nuevo_estado = max(estado_actual - 4, 0)
        elif accion == 1:  # Abajo
            nuevo_estado = min(estado_actual + 4, num_estados - 1)
        elif accion == 2:  # Izquierda
            nuevo_estado = max(estado_actual - 1, 0)
        else:  # Derecha
            nuevo_estado = min(estado_actual + 1, num_estados - 1)

        estado_actual = nuevo_estado

        dibujar(estado_actual)

# Ejecutar la navegación del agente entrenado
navegar_agente()
