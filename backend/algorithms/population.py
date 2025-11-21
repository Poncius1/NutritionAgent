import random

# ======================================================
# 1. Filtrar alimentos compatibles
# (solo aplica restricciones que dependen del alimento)
# ======================================================
def filter_compatible_foods(foods, user):
    """
    Filtra alimentos según restricciones estrictas del usuario.
    - Vegano: eliminar alimentos de origen animal.
    - Alergias: eliminar alimentos cuyo nombre contenga el alergeno.
    * Diabetes e hipertensión NO deben filtrarse aquí, se manejan en fitness.
    """
    filtered = []

    for food in foods:

        # Vegano
        if user.condition == "vegan":
            if food.get("origen") == "animal":
                continue

        # Alergias
        if user.allergies:
            name = food.get("name", "").lower()
            if any(a.lower() in name for a in user.allergies):
                continue

        filtered.append(food)

    return filtered


# ======================================================
# 2. Generar individuo aleatorio (lista de IDs)
# ======================================================
def generate_random_individual(foods, min_items=5, max_items=12):
    """
    Selecciona aleatoriamente entre 5 y 12 alimentos.
    Devuelve una lista de IDs.
    """
    k = random.randint(min_items, max_items)
    selection = random.sample(foods, k)
    return [f["id"] for f in selection]


# ======================================================
# 3. Generar población inicial para el GA
# ======================================================
def generate_initial_population(foods, user, requirements, size=40):
    """
    Genera una población inicial diversa y viable:
    - Se filtran alimentos incompatibles (vegano, alergias).
    - Se asegura que los individuos tengan calorías razonables.
    - Se evita que la población tenga duplicados.
    """
    print(f"[population] Generando población inicial de {size} individuos...")

    # 1) Aplicar restricciones duras
    foods = filter_compatible_foods(foods, user)

    # Convertir a dict id → alimento para cálculos rápidos
    foods_dict = {f["id"]: f for f in foods}

    if len(foods) < 15:
        print("Muy pocos alimentos disponibles después de filtrar.")
        print("La población será poco diversa.")

    population = set()  # set para evitar duplicados

    attempts = 0
    max_attempts = size * 20  # evitar bucles infinitos

    while len(population) < size and attempts < max_attempts:
        attempts += 1

        ind = generate_random_individual(foods)

        # Calorías del individuo
        calories = sum(foods_dict[f_id]["energy"] for f_id in ind)

        # Debe tener al menos 40%-50% del objetivo calórico,
        # para que el GA pueda mejorar
        if calories < requirements["tdee"] * 0.40:
            continue

        # Convertir a tupla para poder agregar al set sin duplicados
        population.add(tuple(ind))

    # Convertimos de vuelta a listas
    final_population = [list(ind) for ind in population]

    print(f"[population] Población final generada: {len(final_population)} individuos.")
    return final_population
