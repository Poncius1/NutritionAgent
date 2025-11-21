

def calculate_user_requirements(user):
    """
    Calcula los requerimientos nutricionales usando:
    - Fórmulas proporcionado (Mifflin-St Jeor, Katch-McArdle)
    - Factores de actividad física oficiales
    - Porcentajes de macros según OMS/NOM/FAO
    """

    weight = user.weight
    height = user.height
    age = user.age
    sex = user.sex

    # ================================================
    #  SELECCIÓN AUTOMÁTICA DE LA FÓRMULA DE TMB
    # ================================================
    if user.fat_percentage is not None:
        # Katch–McArdle (solo si tiene % de grasa)
        F = user.fat_percentage / 100
        lean_mass = weight * (1 - F)
        tmb = 370 + 21.6 * lean_mass   # PDF page 2
        formula_used = "Katch–McArdle"
    else:
        # Mifflin–St Jeor (PDF page 1, más precisa)
        if sex == "male":
            tmb = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            tmb = (10 * weight) + (6.25 * height) - (5 * age) - 161
        formula_used = "Mifflin–St Jeor"

    # ================================================
    #  FACTOR DE ACTIVIDAD FÍSICA
    # ================================================
    activity_map = {
        "0-1": 1.2,
        "2-3": 1.375,
        "4-5": 1.55,
        "6-7": 1.725,
        "extreme": 1.9
    }

    af = activity_map.get(user.exercise, 1.2)

    # TDEE = TMB × factor (PDF)
    tdee = tmb * af

    # ================================================
    #  MACRONUTRIENTES 
    # ================================================
    # Proteína mínima OMS: 0.8 g/kg
    protein_min = 0.8 * weight

    # Rango saludable según PDF:
    # Proteínas: 10–35% de calorías
    protein_cal_low = tdee * 0.10
    protein_cal_high = tdee * 0.35
    protein_g_low = protein_cal_low / 4
    protein_g_high = protein_cal_high / 4

    # Recomendar el punto medio
    protein_g = (protein_g_low + protein_g_high) / 2

    # Carbohidratos: 55–60% (PDF)
    carbs_cal = tdee * 0.575
    carbs_g = carbs_cal / 4

    # Grasas: 20–30% (PDF)
    fat_cal = tdee * 0.25
    fat_g = fat_cal / 9

    # Azúcar <10% (OMS/PDF)
    sugar_cal_limit = tdee * 0.10
    sugar_g_limit = sugar_cal_limit / 4

    # ================================================
    #  SODIO / SAL
    #  < 5 gramos sal/día ≈ 2000 mg sodio
    # ================================================
    sodium_limit_mg = 2000

    if user.condition == "hypertension":
        sodium_limit_mg = 1500  # estándar clínico

    # ================================================
    #  AGUA
    #  ~3 litros total (1.5 agua + 1.5 alimentos)
    # ================================================
    water_l = 3.0

    # ================================================
    # RETORNO COMPLETO
    # ================================================
    return {
        "formula_used": formula_used,
        "tmb": round(tmb, 2),
        "tdee": round(tdee, 2),

        # macronutrientes
        "protein_g": round(protein_g, 2),
        "carbs_g": round(carbs_g, 2),
        "fat_g": round(fat_g, 2),
        "sugar_g_limit": round(sugar_g_limit, 2),
        
        # sal/sodio
        "sodium_mg": sodium_limit_mg,

        # agua
        "water_l": water_l,
    }
