import random
from services.fitness import diet_fitness


# ================================================================
# 1. Reproducción con seguridad de longitudes
# ================================================================
def reproduce(x, y, min_len=5, max_len=12):
    """
    REPRODUCE(x,y) del AIMA, ajustado para mantener longitudes válidas.
    """
    n = min(len(x), len(y))

    if n < 2:
        return x[:]  # fallback seguro

    c = random.randint(1, n - 1)
    child = x[:c] + y[c:]

    # Ajustar longitud
    if len(child) < min_len:
        # rellenar con genes del padre o madre
        filler = random.sample(y, min_len - len(child))
        child.extend(filler)

    if len(child) > max_len:
        child = random.sample(child, max_len)

    return child


# ================================================================
# 2. Mutación
# ================================================================
def mutate(individual, foods_ids, mutation_rate=0.05):
    """
    Mutación: reemplaza un gen por otro alimento válido.
    """
    if random.random() < mutation_rate:
        idx = random.randrange(len(individual))
        individual[idx] = random.choice(foods_ids)
    return individual


# ================================================================
# 3. Selección por ruleta
# ================================================================
def weighted_random_selection(population, fitnesses):
    total = sum(fitnesses)
    if total == 0:
        return random.choice(population)

    r = random.uniform(0, total)
    acc = 0

    for ind, fit in zip(population, fitnesses):
        acc += fit
        if acc >= r:
            return ind

    return population[-1]


# ================================================================
# 4. Algoritmo genético completo
# ================================================================
def genetic_algorithm(
    population,
    foods_dict,
    user,
    requirements,
    generations=50,
    mutation_rate=0.05,
    elite_size=2,
    top_k=5,
):
    foods_ids = list(foods_dict.keys())

    for gen in range(generations):

        # 1) Fitness actual
        fitnesses = [
            diet_fitness(ind, foods_dict, requirements, user)
            for ind in population
        ]

        # 2) Elitismo
        elite = [
            ind for _, ind in sorted(
                zip(fitnesses, population),
                key=lambda x: x[0],
                reverse=True
            )
        ][:elite_size]

        # 3) Nueva generación
        new_population = elite[:]  # conservar los mejores

        while len(new_population) < len(population):
            # Selección
            x = weighted_random_selection(population, fitnesses)
            y = weighted_random_selection(population, fitnesses)

            # Reproducción
            child = reproduce(x, y)

            # Mutación
            child = mutate(child, foods_ids, mutation_rate)

            new_population.append(child)

        population = new_population

    # ==========================================
    # Final: seleccionar mejores para recocido
    # ==========================================
    final_fitnesses = [
        diet_fitness(ind, foods_dict, requirements, user)
        for ind in population
    ]

    sorted_pop = [
        ind for _, ind in sorted(
            zip(final_fitnesses, population),
            key=lambda x: x[0],
            reverse=True
        )
    ]

    return sorted_pop[:top_k]
