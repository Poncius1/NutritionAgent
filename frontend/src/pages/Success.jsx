import { useLocation, useNavigate } from "react-router-dom";
import LayoutGeneral from "../components/LayoutGeneral";
import ProgressSteps from "../components/ProgressSteps";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";

function formatNumber(value, digits = 1) {
  if (value === null || value === undefined) return "—";
  if (typeof value !== "number") return String(value);
  return value.toFixed(digits);
}

function Success() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state?.dietResult;

  // Si entran directo a /success sin tener datos
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

  // ====== DESCARGAR PDF ======
  const handleDownloadPdf = () => {
  const doc = new jsPDF();

  doc.setFontSize(16);
  doc.text("Propuesta nutricional", 14, 18);

  doc.setFontSize(12);
  doc.text("Requerimientos diarios", 14, 26);

  // Columna izquierda: generales
// 📌 Columna izquierda: generales
const generalLines = [
  `Fórmula usada: ${req.formula_used || "—"}`,
  `TMB: ${formatNumber(req.tmb, 2)} kcal`,
  `TDEE: ${formatNumber(req.tdee, 2)} kcal`,
];

// 📌 Columna derecha: régimen alimenticio diario
const regimenLines = [
  `Régimen alimenticio`,
  `Proteína: ${formatNumber(req.protein_g, 1)} g/día`,
  `Carbohidratos: ${formatNumber(req.carbs_g, 1)} g/día`,
  `Grasas: ${formatNumber(req.fat_g, 1)} g/día`,
  `Azúcares añadidos (máx): ${formatNumber(req.sugar_g_limit, 1)} g/día`,
  `Sodio máximo: ${formatNumber(req.sodium_mg, 0)} mg/día`,
  `Agua recomendada: ${formatNumber(req.water_l, 1)} L/día`,
];

let yGeneral = 34;
let yRegimen = 34;

doc.setFontSize(10);

generalLines.forEach((line) => {
  doc.text(line, 14, yGeneral);
  yGeneral += 6;
});

regimenLines.forEach((line, index) => {
  if (index === 0) {
    doc.setFont(undefined, "bold");
    doc.text(line, 110, yRegimen);
    doc.setFont(undefined, "normal");
  } else {
    doc.text(line, 110, yRegimen);
  }
  yRegimen += 6;
});

// 📌 Notas TMB y TDEE
const notesStart = Math.max(yGeneral, yRegimen) + 6;

doc.setFontSize(9);
doc.text(
  "• TMB: Tasa metabólica basal (energía que tu cuerpo necesita en reposo).",
  14,
  notesStart
);
doc.text(
  "• TDEE: Gasto energético diario total considerando tu actividad física.",
  14,
  notesStart + 6
);

const nextY = notesStart + 12;

  // Tabla de alimentos recomendados
  const tableColumns = [
    "Alimento",
    "Carbohidratos (g)",
    "Energía (kcal)",
    "Grasas (g)",
    "Proteínas (g)",
    "Sodio (mg)",
  ];

  const tableRows = foods.map((food) => [
    food.name,
    formatNumber(food.carbs, 1),
    formatNumber(food.energy, 1),
    formatNumber(food.fat, 1),
    formatNumber(food.protein, 1),
    food.sodium === null || food.sodium === undefined
      ? "—"
      : formatNumber(food.sodium, 0),
  ]);

  autoTable(doc, {
    head: [tableColumns],
    body: tableRows,
    startY: nextY + 4,
    styles: { fontSize: 8 },
    headStyles: { fillColor: [20, 130, 120] }, // verde-azulado
  });

  doc.save("propuesta-nutricional.pdf");
};


  return (
    <LayoutGeneral>
      <div className="bg-white rounded-card shadow-card p-4 sm:p-6 md:p-8">
        {/* Cerrar sesión */}
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

        {/* =================== REQUERIMIENTOS =================== */}
<section className="mb-8">
  <div className="bg-nutrition-lightBlue/10 border border-nutrition-lightBlue/40 rounded-2xl p-4 sm:p-5">
    <h2 className="text-lg font-semibold text-nutrition-darkBlue mb-3">
      Requerimientos diarios
    </h2>

    <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-4 text-sm text-gray-700">

      {/* 📌 Columna 1: Datos generales */}
      <div className="space-y-1">
        <p>
  <span className="font-medium">Fórmula usada:</span>{" "}
  <span className="font-semibold">{req.formula_used || "—"}</span>
</p>
        <p>
          <span className="font-medium">TMB:</span>{" "}
          {formatNumber(req.tmb, 2)} kcal
        </p>
        <p>
          <span className="font-medium">TDEE:</span>{" "}
          {formatNumber(req.tdee, 2)} kcal
        </p>
      </div>

      {/* 📌 Columna 2: Régimen alimenticio diario */}
      <div className="space-y-1">
        <p className="font-semibold text-nutrition-darkBlue">
          Régimen alimenticio
        </p>
        <p>
          <span className="font-medium">Proteína:</span>{" "}
          {formatNumber(req.protein_g, 1)} g/día
        </p>
        <p>
          <span className="font-medium">Carbohidratos:</span>{" "}
          {formatNumber(req.carbs_g, 1)} g/día
        </p>
        <p>
          <span className="font-medium">Grasas:</span>{" "}
          {formatNumber(req.fat_g, 1)} g/día
        </p>
        <p>
          <span className="font-medium">Azúcares añadidos (máx):</span>{" "}
          {formatNumber(req.sugar_g_limit, 1)} g/día
        </p>
        <p>
          <span className="font-medium">Sodio máximo:</span>{" "}
          {formatNumber(req.sodium_mg, 0)} mg/día
        </p>
        <p>
          <span className="font-medium">Agua recomendada:</span>{" "}
          {formatNumber(req.water_l, 1)} L/día
        </p>
      </div>
    </div>

    {/* 📌 Notas explicativas */}
    <div className="mt-4 p-3 rounded-xl bg-gray-50 border border-gray-200">
      <p className="text-xs text-gray-600 mb-1">
        <strong>TMB:</strong> Tasa metabólica basal (energía que tu cuerpo
        necesita en reposo).
      </p>
      <p className="text-xs text-gray-600">
        <strong>TDEE:</strong> Gasto energético diario total considerando tu
        actividad física.
      </p>
    </div>
  </div>
</section>

        {/* =================== ALIMENTOS =================== */}
        <section>
          <h2 className="text-lg font-semibold text-nutrition-darkBlue mb-3">
            Alimentos recomendados
          </h2>

          <div className="overflow-x-auto rounded-2xl border border-gray-200 bg-white">
            <table className="min-w-full text-sm text-left">
              <thead className="bg-nutrition-teal text-white">
                <tr>
                  {/* 👇 Sin columna ID */}
                  <th className="px-4 py-2 font-semibold">Alimento</th>
                  <th className="px-4 py-2 font-semibold">
                    Carbohidratos (g)
                  </th>
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
                      colSpan={6}
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

        {/* =================== BOTONES =================== */}
        <div className="mt-8 flex flex-col sm:flex-row justify-end gap-3">
          <button
            onClick={handleDownloadPdf}
            className="inline-flex items-center justify-center px-6 py-2.5 rounded-full text-sm font-semibold text-nutrition-blue bg-white border border-nutrition-blue hover:bg-nutrition-lightBlue/20 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-nutrition-yellow"
          >
            Descargar PDF
          </button>

          <button
            onClick={() => navigate("/")}
            className="inline-flex items-center justify-center px-6 py-2.5 rounded-full text-sm font-semibold text-white bg-nutrition-blue hover:bg-nutrition-darkBlue focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-nutrition-yellow"
          >
            Salir
          </button>
        </div>
      </div>
    </LayoutGeneral>
  );
}

export default Success;