"""
    Calcula qué tan buena es una combinación de alimentos.
    individual: lista de IDs de alimentos
    foods_dict: diccionario id → alimento
    requirements: requerimientos (cal, macros, sodio)
    user: UserInput
    """

def diet_fitness(individual, foods_dict, requirements, user):
   

    # ============================================
    # 1. Convertir IDs a alimentos reales
    # ============================================
    items = [foods_dict[food_id] for food_id in individual if food_id in foods_dict]

    if len(items) == 0:
        return 0

    # ============================================
    # 2. Sumar nutrientes
    # ============================================
    totals = {
        "calories": sum(x["energy"]  for x in items),
        "protein":  sum(x["protein"] for x in items),
        "carbs":    sum(x["carbs"]   for x in items),
        "fat":      sum(x["fat"]     for x in items),
        "sodium":   sum(x.get("sodium", 0) for x in items),
    }

    # ============================================
    # 3. Error relativo (entre 0 y 1)
    # ============================================
    def rel_error(target, actual):
        if target == 0:
            return 0
        return abs(actual - target) / target

    target_cal = requirements.get("calories") or requirements["tdee"]
    e_cal = rel_error(target_cal, totals["calories"])
    e_pro  = rel_error(requirements["protein_g"], totals["protein"])
    e_carb = rel_error(requirements["carbs_g"], totals["carbs"])
    e_fat  = rel_error(requirements["fat_g"], totals["fat"])

    # ============================================
    # 4. Penalizaciones médicas
    # ============================================
    penalty = 0

    #  Hipertensión  <2000 mg/día 
    if user.condition == "hypertension":
        if totals["sodium"] > requirements["sodium_mg"]:
            diff = totals["sodium"] - requirements["sodium_mg"]
            penalty += diff / 2000  # penalización suave

    # Diabetes  exceso de carbohidratos totales
    # (NO puedes usar azúcares simples porque tu dataset no los contiene)
    if user.condition == "diabetes":
        if totals["carbs"] > requirements["carbs_g"]:
            diff = totals["carbs"] - requirements["carbs_g"]
            penalty += diff / 300  # ajustado, más realista

    #  Vegano → si hay un alimento animal  dieta inválida
    if user.condition == "vegan":
        for item in items:
            if item.get("origen") == "animal":
                return 0

    # ============================================
    # 5. Errores totales + penalización médica
    # ============================================
    total_error = e_cal + e_pro + e_carb + e_fat + penalty

    # ============================================
    # 6. Convertir a fitness (0 a 1)
    # ============================================
    fitness = 1 - total_error

    return max(0, min(1, fitness))
