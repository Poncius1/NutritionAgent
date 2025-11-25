const steps = [
  { id: 1, label: "Datos del usuario" },
  { id: 2, label: "Estilo de vida" },
  { id: 3, label: "Revisión" },
];

function ProgressSteps({ currentStep = 1 }) {
  return (
    <div className="mb-6">

      <div className="flex items-center gap-3">
        {steps.map((step, index) => {
          const isActive = step.id === currentStep;
          const isCompleted = step.id < currentStep;

          return (
            <div key={step.id} className="flex items-center flex-1">
              <div className="flex flex-col items-center">
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
                    "mt-1 text-xs sm:text-sm",
                    isActive ? "text-nutrition-darkBlue" : "text-gray-400",
                  ].join(" ")}
                >
                  {step.label}
                </p>
              </div>

              {index < steps.length - 1 && (
                <div className="flex-1 h-px mx-2 sm:mx-4 bg-gray-200" />
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default ProgressSteps;