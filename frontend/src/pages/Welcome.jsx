import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../components/Layout";

function isValidEmail(email) {
  // validación simple
  return /\S+@\S+\.\S+/.test(email);
}

function Welcome() {
  const [email, setEmail] = useState("");
  const [touched, setTouched] = useState(false);
  const navigate = useNavigate();

  const valid = isValidEmail(email);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!valid) return;

    // Si quieres usarlo después en el backend o formularios:
    sessionStorage.setItem("userEmail", email);

    navigate("/intake");
  };

  return (
    <Layout>
      <div className="bg-white rounded-card shadow-card px-6 py-8 sm:px-10 sm:py-10 relative overflow-hidden">
        {/* "Decoración" tipo cards flotantes */}
        <div className="pointer-events-none absolute -top-6 -left-8 w-28 h-28 rounded-2xl bg-nutrition-yellow/70 blur-md opacity-60" />
        <div className="pointer-events-none absolute -bottom-8 -right-10 w-40 h-40 rounded-full bg-nutrition-teal/40 blur-xl opacity-70" />

        {/* Hero */}
        <main className="relative z-10">
          <div className="text-center max-w-2xl mx-auto mb-8">
            <h1 className="text-2xl sm:text-3xl md:text-4xl font-semibold text-gray-900 mb-2 leading-tight">
              Bienvenido a{" "}
              <span className="text-nutrition-blue">PAAI</span>
            </h1>
            <p className="text-lg sm:text-xl md:text-2xl text-gray-700 mb-2">
              Evalúa tu estado nutricional con la ayuda de IA
            </p>
            <p className="text-sm sm:text-base text-gray-500">
              Ingresa tu correo electrónico para comenzar y recibir un resumen personalizado
              de tus datos nutricionales.
            </p>
          </div>

          {/* Formulario de correo */}
          <form
            onSubmit={handleSubmit}
            className="max-w-md mx-auto flex flex-col sm:flex-row gap-3 items-stretch sm:items-center"
          >
            <div className="flex-1">
              <label
                htmlFor="email"
                className="block text-xs font-medium text-gray-600 mb-1 text-left"
              >
                Correo electrónico
              </label>
              <input
                id="email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                onBlur={() => setTouched(true)}
                placeholder="tucorreo@ejemplo.com"
                className={[
                  "block w-full rounded-full border px-4 py-2.5 text-sm bg-white focus:outline-none focus:ring-2",
                  valid
                    ? "border-gray-300 focus:ring-nutrition-blue focus:border-nutrition-blue"
                    : touched && email.length > 0
                    ? "border-nutrition-orange focus:ring-nutrition-orange/70"
                    : "border-gray-300 focus:ring-nutrition-blue focus:border-nutrition-blue",
                ].join(" ")}
              />
              {!valid && touched && email.length > 0 && (
                <p className="mt-1 text-xs text-nutrition-orange text-left">
                  Ingresa un correo válido.
                </p>
              )}
            </div>

            <button
              type="submit"
              disabled={!valid}
              className={[
                "inline-flex justify-center items-center whitespace-nowrap rounded-full px-5 py-2.5 text-sm font-semibold shadow-sm",
                valid
                  ? "bg-nutrition-blue text-white hover:bg-nutrition-darkBlue focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-nutrition-yellow"
                  : "bg-gray-200 text-gray-500 cursor-not-allowed",
              ].join(" ")}
            >
              Continuar
              <span className="ml-1.5 text-lg">→</span>
            </button>
          </form>

          <p className="mt-4 text-xs text-gray-400 text-center">
            Al continuar aceptas recibir información relacionada con tu evaluación nutricional.
          </p>
        </main>
      </div>
    </Layout>
  );
}

export default Welcome;