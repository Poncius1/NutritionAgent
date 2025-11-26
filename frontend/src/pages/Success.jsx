import { useLocation, useNavigate } from "react-router-dom";
import LayoutGeneral from "../components/LayoutGeneral";
import ProgressSteps from "../components/ProgressSteps";

function formatNumber(value, digits = 1) {
  if (value === null || value === undefined) return "—";
  if (typeof value !== "number") return String(value);
  return value.toFixed(digits);
}

function Success() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state?.dietResult;

  // Fallback por si llegan directo a /success sin haber llenado el form
  if (!result) {
    return (
      <LayoutGeneral>
        <div className="bg-white rounded-card shadow-card p-6 sm:p-8 text-center">
          <h1 className="text-xl sm:text-2xl font-semibold text-nutrition-darkBlue mb-2">
            No hay resultados disponibles
          </h1>
          <p className="text-sm text-gray-600 mb-6">
            Para ver tu propuesta nutricional, primero completa el cuestionario.
          </p>
          <button
            onClick={() => navigate("/")}
            className="inline-flex items-center justify-center px-6 py-2.5 rounded-full text-sm font-semibold text-white bg-nutrition-blue hover:bg-nutrition-darkBlue focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-nutrition-yellow"
          >
            Volver al inicio
          </button>
        </div>
      </LayoutGeneral>
    );
  }

  const req = result.requirements || {};
  const foods = result.final_diet || [];

  return (
    <LayoutGeneral>
      <div className="bg-white rounded-card shadow-card p-4 sm:p-6 md:p-8">
        {/* Header superior con pasos */}
        <button
          className="flex items-center gap-2 text-sm text-nutrition-blue hover:text-nutrition-darkBlue mb-4"
          onClick={() => navigate("/")}
        >
          <span className="text-base">←</span>
          Cerrar sesión
        </button>

        <ProgressSteps currentStep={2} />

        <h1 className="text-xl sm:text-2xl font-semibold text-nutrition-darkBlue mb-2">
          Tu propuesta nutricional
        </h1>
        <p className="text-sm text-gray-500 mb-6">
          Estos son tus requerimientos diarios estimados y una selección de
          alimentos recomendados basada en tus necesidades.
        </p>

        {/* Requerimientos diarios */}
        <section className="mb-8">
          <div className="bg-nutrition-lightBlue/10 border border-nutrition-lightBlue/40 rounded-2xl p-4 sm:p-5">
            <h2 className="text-lg font-semibold text-nutrition-darkBlue mb-3">
              Requerimientos diarios
            </h2>
            <ul className="text-sm text-gray-700 space-y-1">
              <li>
                <span className="font-medium">Fórmula usada:</span>{" "}
                {req.formula_used || "—"}
              </li>
              <li>
                <span className="font-medium">TMB:</span>{" "}
                {formatNumber(req.tmb, 2)} kcal
              </li>
              <li>
                <span className="font-medium">TDEE:</span>{" "}
                {formatNumber(req.tdee, 2)} kcal
              </li>
              <li>
                <span className="font-medium">Proteína:</span>{" "}
                {formatNumber(req.protein_g, 1)} g/día
              </li>
              <li>
                <span className="font-medium">Carbohidratos:</span>{" "}
                {formatNumber(req.carbs_g, 1)} g/día
              </li>
              <li>
                <span className="font-medium">Grasas:</span>{" "}
                {formatNumber(req.fat_g, 1)} g/día
              </li>
              <li>
                <span className="font-medium">
                  Límite de azúcares añadidos:
                </span>{" "}
                {formatNumber(req.sugar_g_limit, 1)} g/día
              </li>
              <li>
                <span className="font-medium">Sodio máximo:</span>{" "}
                {formatNumber(req.sodium_mg, 0)} mg/día
              </li>
              <li>
                <span className="font-medium">Agua recomendada:</span>{" "}
                {formatNumber(req.water_l, 1)} L/día
              </li>
            </ul>
          </div>
        </section>

        {/* Alimentos recomendados */}
        <section>
          <h2 className="text-lg font-semibold text-nutrition-darkBlue mb-3">
            Alimentos recomendados
          </h2>

          <div className="overflow-x-auto rounded-2xl border border-gray-200 bg-white">
            <table className="min-w-full text-sm text-left">
              <thead className="bg-nutrition-teal text-white">
                <tr>
                  <th className="px-4 py-2 font-semibold">ID</th>
                  <th className="px-4 py-2 font-semibold">Alimento</th>
                  <th className="px-4 py-2 font-semibold">Carbohidratos (g)</th>
                  <th className="px-4 py-2 font-semibold">Energía (kcal)</th>
                  <th className="px-4 py-2 font-semibold">Grasas (g)</th>
                  <th className="px-4 py-2 font-semibold">Proteínas (g)</th>
                  <th className="px-4 py-2 font-semibold">Sodio (mg)</th>
                </tr>
              </thead>
              <tbody>
                {foods.map((food, index) => (
                  <tr
                    key={food.id ?? index}
                    className={
                      index % 2 === 0
                        ? "bg-white"
                        : "bg-nutrition-lightBlue/5"
                    }
                  >
                    <td className="px-4 py-2 whitespace-nowrap text-gray-700">
                      {food.id}
                    </td>
                    <td className="px-4 py-2 text-gray-800">{food.name}</td>
                    <td className="px-4 py-2 text-gray-700">
                      {formatNumber(food.carbs, 1)}
                    </td>
                    <td className="px-4 py-2 text-gray-700">
                      {formatNumber(food.energy, 1)}
                    </td>
                    <td className="px-4 py-2 text-gray-700">
                      {formatNumber(food.fat, 1)}
                    </td>
                    <td className="px-4 py-2 text-gray-700">
                      {formatNumber(food.protein, 1)}
                    </td>
                    <td className="px-4 py-2 text-gray-700">
                      {food.sodium === null || food.sodium === undefined
                        ? "—"
                        : formatNumber(food.sodium, 0)}
                    </td>
                  </tr>
                ))}

                {foods.length === 0 && (
                  <tr>
                    <td
                      colSpan={7}
                      className="px-4 py-4 text-center text-gray-500"
                    >
                      No se encontraron alimentos recomendados en el resultado.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </section>

        {/* Botón salir */}
        <div className="mt-8 flex justify-end">
          <button
            onClick={() => navigate("/")}
            className="inline-flex items-center justify-center px-6 py-2.5 rounded-full text-sm font-semibold text-nutrition-blue bg-white border border-nutrition-blue hover:bg-nutrition-lightBlue/20 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-nutrition-yellow"
          >
            Salir
          </button>
        </div>
      </div>
    </LayoutGeneral>
  );
}

export default Success;