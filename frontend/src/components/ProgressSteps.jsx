const steps = [
  { id: 1, label: "Datos del usuario" },
  { id: 2, label: "Revisión" },
];

function ProgressSteps({ currentStep = 1 }) {
  return (
    <div className="mb-6">

      {/* Contenedor centrado y espaciado */}
      <div className="flex justify-between w-full max-w-md mx-auto">

        {steps.map((step, index) => {
          const isActive = step.id === currentStep;
          const isCompleted = step.id < currentStep;

          return (
            <div key={step.id} className="flex flex-col items-center flex-1">

              <div
                className={[
                  "flex items-center justify-center w-8 h-8 rounded-full border-2 text-xs font-semibold",
                  isCompleted
                    ? "bg-nutrition-teal border-nutrition-teal text-white"
                    : isActive
                    ? "border-nutrition-blue text-nutrition-blue bg-white"
                    : "border-gray-300 text-gray-400 bg-white",
                ].join(" ")}
              >
                {isCompleted ? "✓" : step.id}
              </div>

              <p
                className={[
                  "mt-1 text-xs sm:text-sm text-center",
                  isActive ? "text-nutrition-darkBlue" : "text-gray-400",
                ].join(" ")}
              >
                {step.label}
              </p>

              {/* Línea entre pasos */}
              {index < steps.length - 1 && (
                <div className="h-px w-full bg-gray-200 mt-2" />
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default ProgressSteps;