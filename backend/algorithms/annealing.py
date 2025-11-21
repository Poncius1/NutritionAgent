import math
import random
from services.fitness import diet_fitness


def neighbor(individual, foods_ids, min_len=5, max_len=12):
    new_ind = individual[:]
    op = random.choice(["add", "remove", "replace"])

    if op == "add" and len(new_ind) < max_len:
        new_gene = random.choice(foods_ids)
        if new_gene not in new_ind:
            new_ind.append(new_gene)

    elif op == "remove" and len(new_ind) > min_len:
        idx = random.randrange(len(new_ind))
        new_ind.pop(idx)

    else:
        idx = random.randrange(len(new_ind))
        new_gene = random.choice(foods_ids)
        if new_gene not in new_ind:
            new_ind[idx] = new_gene

    return new_ind


def simulated_annealing(
    individual,
    foods_dict,
    requirements,
    user,
    temp_start=1.0,
    temp_end=0.001,
    alpha=0.97,
    steps_per_temp=50
):

    current = individual[:]
    best = current[:]

    foods_ids = list(foods_dict.keys())

    current_score = diet_fitness(current, foods_dict, requirements, user)
    if math.isnan(current_score) or math.isinf(current_score):
        current_score = 0

    best_score = current_score

    temperature = temp_start
    print(f"SA | Inicio con fitness inicial: {current_score:.4f}")

    while temperature > temp_end:

        for _ in range(steps_per_temp):

            candidate = neighbor(current, foods_ids)

            # 🔥 PROTECCIÓN 1: nunca usar dietas menores a 5 alimentos
            if len(candidate) < 5:
                continue

            candidate_score = diet_fitness(candidate, foods_dict, requirements, user)

            # 🔥 PROTECCIÓN 2: evitar NaN / Inf
            if math.isnan(candidate_score) or math.isinf(candidate_score):
                candidate_score = 0

            delta = candidate_score - current_score

            if delta > 0:
                current = candidate
                current_score = candidate_score

                if candidate_score > best_score:
                    best = candidate
                    best_score = candidate_score

            else:
                prob = math.exp(delta / temperature)
                if random.random() < prob:
                    current = candidate
                    current_score = candidate_score

        temperature *= alpha

    print(f"SA | Mejor dieta final fitness={best_score:.4f}")
    return best, best_score
