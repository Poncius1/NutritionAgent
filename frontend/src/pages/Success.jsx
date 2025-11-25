import Layout from "../components/Layout";
import ProgressSteps from "../components/ProgressSteps";
import { useNavigate } from "react-router-dom";

function Success() {
  const navigate = useNavigate();

  return (
    <Layout>
      <div className="bg-white rounded-card shadow-card p-5 sm:p-6 md:p-8 max-w-lg mx-auto">
        {/* Stepper en el paso 3 */}
        <ProgressSteps currentStep={3} />

        <div className="mt-8 bg-nutrition-blue text-white rounded-3xl px-6 py-8 sm:px-8 sm:py-10 relative overflow-hidden">

          {/* confetti / glow simple */}
          <div className="pointer-events-none absolute -top-10 -left-10 w-32 h-32 rounded-full bg-white/10 blur-xl" />
          <div className="pointer-events-none absolute -bottom-12 -right-12 w-40 h-40 rounded-full bg-nutrition-teal/40 blur-2xl" />

          {/* “Ilustración” */}
          <div className="relative z-10 flex flex-col items-center text-center">
            <div className="w-16 h-16 rounded-full bg-white/15 flex items-center justify-center mb-4">
              <span className="text-3xl">🎉</span>
            </div>

            <h1 className="text-xl sm:text-2xl font-semibold mb-2">
              ¡Lo lograste, buen trabajo!
            </h1>

            <p className="text-sm sm:text-base text-white/80 mb-6 max-w-md">
              Has completado el primer paso hacia una vida más saludable. 
              Gracias por compartir tu información, esto nos ayuda a crear 
              recomendaciones pensadas especialmente para ti.
            </p>

            {/* “Tarjeta” de mensaje IA */}
            <div className="bg-white text-nutrition-darkBlue rounded-2xl px-4 py-5 sm:px-5 sm:py-6 shadow-md w-full">
              <p className="text-sm sm:text-base text-center">
                Un agente de <span className="font-semibold">IA especializada en nutrición</span> 
                está analizando tus respuestas para preparar una propuesta personalizada.  
                <br />
                <span className="font-medium">
                  En breve recibirás un correo con todos los detalles y siguientes pasos.
                </span>
              </p>
            </div>

            {/* Botón salir */}
            <button
              onClick={() => {
                sessionStorage.removeItem("userEmail");
                navigate("/");
              }}
              className="mt-6 w-full bg-white text-nutrition-blue font-semibold text-sm sm:text-base py-3 rounded-full shadow-sm hover:bg-gray-50"
            >
              Salir
            </button>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default Success;