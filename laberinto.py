import numpy as np

# Definición del laberinto: 0 representa un espacio libre, 1 representa un obstáculo, y 2 representa la salida.
maze = np.array([
    [0, 0, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 2]
])

# Definición de parámetros
num_episodes = 1000 
learning_rate = 0.1
discount_factor = 0.9
exploration_prob = 0.2

# Obtener las dimensiones del laberinto
num_rows, num_cols = maze.shape

# Inicializar la tabla Q con valores aleatorios
q_table = np.random.rand(num_rows, num_cols, 4)

# Definir acciones posibles (arriba, abajo, izquierda, derecha)
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Función para seleccionar una acción basada en la estrategia epsilon-greedy
def select_action(state):
    if np.random.rand() < exploration_prob:
        return np.random.choice(4)
    else:
        return np.argmax(q_table[state[0], state[1]])

# Entrenamiento del agente
for episode in range(num_episodes):
    state = (0, 0)
    done = False

    while not done:
        action = select_action(state)
        next_state = (state[0] + actions[action][0], state[1] + actions[action][1])

        if maze[next_state[0], next_state[1]] == 2:  # Llegamos a la salida
            reward = 1
            done = True
        elif maze[next_state[0], next_state[1]] == 1:  # Chocamos contra un obstáculo
            reward = -1
            done = True
        else:
            reward = 0

        q_table[state[0], state[1], action] = q_table[state[0], state[1], action] + \
            learning_rate * (reward + discount_factor *
                             np.max(q_table[next_state]) - q_table[state[0], state[1], action])

        state = next_state

# Al final del entrenamiento, el agente debería haber aprendido una política óptima
# para navegar a través del laberinto. Puedes utilizar esta política para encontrar
# el camino óptimo desde la posición inicial hasta la salida.



def find_path(q_table, maze):
    start_state = (0, 0)
    current_state = start_state
    path = [current_state]

    while maze[current_state[0], current_state[1]] != 2:
        action = np.argmax(q_table[current_state[0], current_state[1]])
        next_state = (current_state[0] + actions[action][0], current_state[1] + actions[action][1])
        path.append(next_state)
        current_state = next_state

    return path

# Llama a esta función después de entrenar al agente para encontrar el camino óptimo.
optimal_path = find_path(q_table, maze)

if maze[optimal_path[-1][0], optimal_path[-1][1]] == 2:
    print("¡El agente encontró la salida!")
    print("Camino óptimo:")
    for state in optimal_path:
        print(state)
else:
    print("El agente no pudo encontrar la salida.")
