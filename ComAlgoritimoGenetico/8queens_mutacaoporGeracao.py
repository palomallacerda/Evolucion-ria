import random
import matplotlib.pyplot as plt

# Função para visualizar o tabuleiro
def view(board):
    for i in range(8):
        for j in range(8):
            if board[i] == j:
                print('[R]', end=' ')
            else:
                print('[ ]', end=' ')
        print()

# Função para calcular o fitness
def fitness(board):
    attacks = 0
    for i in range(8):
        for j in range(i+1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return 28 - attacks

# Função para realizar o cruzamento entre dois tabuleiros
def crossover(board1, board2, crossover_rate):
    if random.random() < crossover_rate:
        split_point = random.randint(1, 7)
        new_board1 = board1[:split_point] + board2[split_point:]
        new_board2 = board2[:split_point] + board1[split_point:]
        return new_board1, new_board2
    else:
        return board1, board2

# Função para realizar a mutação em um tabuleiro
def mutate(board, mutation_rate):
    boardCopy = board.copy()
    if random.random() < mutation_rate:
        index = random.randint(0, 7)
        new_value = random.randint(0, 7)
        boardCopy[index] = new_value
    return boardCopy

# Parâmetros do algoritmo genético
population_size = 100
crossover_rate_min = 0.6
crossover_rate_max = 0.9
mutation_rate_min = 0.05
mutation_rate_max = 0.2
generations = 70

# Inicialização da população
population = []
for i in range(population_size):
    board = [random.randint(0, 7) for j in range(8)]
    population.append(board)

# Execução do algoritmo genético
max_fitness = []
for generation in range(generations):
    # Avaliação do fitness da população
    fitness_scores = [fitness(board) for board in population]
    max_fitness.append(max(fitness_scores))
    
    # Seleção dos pais (torneio de dois)
    parents = []
    for i in range(population_size):
        p1 = random.randint(0, population_size-1)
        p2 = random.randint(0, population_size-1)
        if fitness_scores[p1] > fitness_scores[p2]:
            parents.append(population[p1])
        else:
            parents.append(population[p2])
    
    # Cruzamento e mutação para gerar nova população
    new_population = []
    for i in range(int(population_size/2)):
        p1 = i * 2
        p2 = i * 2 + 1
        
        # Seleção das taxas de cruzamento e mutação para cada indivíduo
        crossover_rate = random.uniform(crossover_rate_min, crossover_rate_max)
        mutation_rate = random.uniform(mutation_rate_min, mutation_rate_max)
        
        offspring1, offspring2 = crossover(parents[p1], parents[p2], crossover_rate)
        offspring1 = mutate(offspring1, mutation_rate)
        offspring2 = mutate(offspring2, mutation_rate)
        new_population.append(offspring1)
        new_population.append(offspring2)
    population = new_population

# Impressão da melhor sol
# Impressão da melhor solução encontrada
best_board = max(population, key=fitness)
print('Melhor solução:')
view(best_board)

# Plot do gráfico de maior fitness por geração
plt.plot(range(generations), max_fitness)
plt.title("Maior fitness por geração com taxas variadas")
plt.ylabel("Fitness")
plt.xlabel("Geração")
plt.show()