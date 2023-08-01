import random

# Population size
POPULATION_SIZE = 100

# Length of the binary sequence
SEQUENCE_LENGTH = 20

# Crossover rate (probability of crossover between two individuals)
CROSSOVER_RATE = 0.8

# Mutation rate (probability of mutation in an individual)
MUTATION_RATE = 0.1

# Number of generations
NUM_GENERATIONS = 100

def create_individual():
    return [random.choice([0, 1]) for _ in range(SEQUENCE_LENGTH)]

def fitness(individual):
    return sum(individual)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, SEQUENCE_LENGTH - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    mutated_individual = individual.copy()
    for i in range(len(mutated_individual)):
        if random.random() < MUTATION_RATE:
            mutated_individual[i] = 1 - mutated_individual[i]  # Flips 0 to 1 or 1 to 0 with 50% probability
    return mutated_individual

def genetic_algorithm():
    population = [create_individual() for _ in range(POPULATION_SIZE)]

    for generation in range(NUM_GENERATIONS):
        population.sort(key=lambda x: -fitness(x))  # Sorts the population by fitness in descending order
        best_individual = population[0]
        print(f"Generation {generation + 1} - Best Fitness: {fitness(best_individual)}")

        new_population = [best_individual]

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.choices(population[:50], k=2)  # Selects two parents randomly from the top 50 individuals
            if random.random() < CROSSOVER_RATE:
                child1, child2 = crossover(parent1, parent2)
                new_population.append(mutate(child1))
                new_population.append(mutate(child2))
            else:
                new_population.append(mutate(parent1))
                new_population.append(mutate(parent2))

        population = new_population

if __name__ == "__main__":
    genetic_algorithm()
