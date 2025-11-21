import math

def diet_fitness(individual, foods_dict, requirements, user):
    """
    Calcula el fitness de una dieta (lista de IDs).
    Devuelve un valor entre 0 y 1, nunca NaN, nunca infinito.
    """

    # ============================================
    # 1. Convertir IDs a alimentos reales
    # ============================================
    items = [foods_dict[food_id] for food_id in individual if food_id in foods_dict]

    if len(items) == 0:
        return 0.0

    # ============================================
    # 2. Sumar nutrientes
    # ============================================
    totals = {
        "calories": sum(float(x["energy"])  for x in items),
        "protein":  sum(float(x["protein"]) for x in items),
        "carbs":    sum(float(x["carbs"])   for x in items),
        "fat":      sum(float(x["fat"])     for x in items),
        "sodium":   sum(float(x.get("sodium", 0)) for x in items),
    }

    # ============================================
    # 3. Targets nutricionales
    # ============================================
    target_cal = requirements.get("calories") or requirements["tdee"]
    target_pro = requirements["protein_g"]
    target_carb = requirements["carbs_g"]
    target_fat = requirements["fat_g"]

    # ============================================
    # 4. Error relativo
    # ============================================
    def rel_error(target, actual):
        if target <= 0:
            return 0
        return abs(actual - target) / target

    e_cal  = rel_error(target_cal, totals["calories"])
    e_pro  = rel_error(target_pro, totals["protein"])
    e_carb = rel_error(target_carb, totals["carbs"])
    e_fat  = rel_error(target_fat, totals["fat"])

    # ============================================
    # 5. Penalizaciones médicas
    # ============================================
    penalty = 0.0

    # ---- Hipertensión: exceso de sodio
    if user.condition == "hypertension":
        limit = requirements["sodium_mg"]
        if totals["sodium"] > limit:
            penalty += (totals["sodium"] - limit) / 2000.0

    # ---- Diabetes: exceso de carbohidratos totales
    if user.condition == "diabetes":
        if totals["carbs"] > target_carb:
            penalty += (totals["carbs"] - target_carb) / 300.0

    # ---- Vegano: si hay alimentos animales → fitness 0
    if user.condition == "vegan":
        for item in items:
            # tu base probablemente no tiene "origen", así que esto evita fallos
            if item.get("origen") == "animal":
                return 0.0

    # ============================================
    # 6. Sumar errores + penalizaciones
    # ============================================
    total_error = e_cal + e_pro + e_carb + e_fat + penalty

    # ============================================
    # 7. Convertir error a fitness (entre 0 y 1)
    # ============================================
    fitness = 1.0 - total_error

    # ============================================
    # 8. Sanitización final
    # ============================================
    # Nunca devolver NaN o infinito
    if math.isnan(fitness) or math.isinf(fitness):
        return 0.0

    # Limitar el fitness entre 0 y 1
    return max(0.0, min(1.0, fitness))
