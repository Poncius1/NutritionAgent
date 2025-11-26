import ProgressSteps from "../components/ProgressSteps";
import FormSection from "../components/FormSection";
import TextInput from "../components/TextInput";
import NumberInput from "../components/NumberInput";
import RadioGroup from "../components/RadioGroup";
import { useUserInputForm } from "../hooks/useUserInputForm";
import LayoutGeneral from "../components/LayoutGeneral";
import { useNavigate } from "react-router-dom";

function UserIntakeForm() {
  const { values, handleChange, handleSubmit, submitting } =
    useUserInputForm();
  const navigate = useNavigate();

  const onSubmit = async (e) => {
    const result = await handleSubmit(e);
    if (result) {
      navigate("/success", { state: { dietResult: result } });
    }
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

        <ProgressSteps currentStep={1} />

        <h1 className="text-xl sm:text-2xl font-semibold text-nutrition-darkBlue mb-2 mt-6">
          Sobre ti
        </h1>
        <p className="text-sm text-gray-500 mb-6">
          Completa la siguiente información para personalizar tus recomendaciones
          nutricionales.
        </p>

        <form className="space-y-8" onSubmit={onSubmit}>
          {/* Datos generales */}
          <FormSection title="Datos generales">
            <TextInput
              id="name"
              label="Nombre"
              required
              value={values.name}
              onChange={handleChange("name")}
              placeholder="Escribe tu nombre"
            />

            <NumberInput
              id="age"
              label="Edad"
              required
              value={values.age}
              onChange={handleChange("age")}
              placeholder="Años"
              min={10}
              max={120}
            />

            <NumberInput
              id="weight"
              label="Peso (kg)"
              required
              value={values.weight}
              onChange={handleChange("weight")}
              placeholder="Ej. 68.5"
              step="0.1"
              min={0.1}
            />

            <NumberInput
              id="height"
              label="Estatura (cm)"
              required
              value={values.height}
              onChange={handleChange("height")}
              placeholder="Ej. 175"
              step="0.1"
              min={0.1}
            />

            <RadioGroup
              name="sex"
              label="Sexo"
              helperText="Selecciona la opción que mejor te describa."
              value={values.sex}
              onChange={handleChange("sex")}
              options={[
                { value: "male", label: "Masculino" },
                { value: "female", label: "Femenino" },
              ]}
            />
          </FormSection>

          {/* Composición corporal */}
          <FormSection
            title="Composición corporal (opcional)"
            description="Si conoces este dato, nos ayudará a afinar tus recomendaciones."
          >
            <NumberInput
              id="fat_percentage"
              label="% grasa corporal"
              helperText="Entre 1 y 60. Deja vacío si no lo conoces."
              value={values.fat_percentage}
              onChange={handleChange("fat_percentage")}
              placeholder="Ej. 18"
              step="0.1"
              min={1}
              max={60}
            />
          </FormSection>

          {/* Estilo de vida */}
          <FormSection title="Estilo de vida y salud">
            <RadioGroup
              name="exercise"
              label="Frecuencia de ejercicio (días por semana)"
              helperText="Selecciona la opción que más se acerque a tu rutina."
              value={values.exercise}
              onChange={handleChange("exercise")}
              options={[
                { value: "0-1", label: "0–1 días" },
                { value: "2-3", label: "2–3 días" },
                { value: "4-5", label: "4–5 días" },
                { value: "6-7", label: "6–7 días" },
                { value: "extreme", label: "Entrenamiento muy intenso" },
              ]}
            />

            <RadioGroup
              name="condition"
              label="Condición de salud principal"
              helperText="Indica la opción que mejor describa tu situación actual."
              value={values.condition}
              onChange={handleChange("condition")}
              options={[
                { value: "none", label: "Ninguna" },
                { value: "diabetes", label: "Diabetes" },
                { value: "hypertension", label: "Hipertensión" },
                { value: "vegan", label: "Alimentación vegana" },
              ]}
            />

            <TextInput
              id="allergies"
              label="Alergias alimentarias"
              helperText="Separa varias con comas. Ej. fresa, maní, mariscos"
              value={values.allergies}
              onChange={handleChange("allergies")}
              placeholder="Escribe tus alergias (si tienes)"
            />
          </FormSection>

          {/* Botón submit */}
          <div className="mt-4 flex justify-end">
            <button
              type="submit"
              disabled={submitting}
              className="inline-flex items-center justify-center px-6 py-2.5 rounded-full text-sm font-semibold text-white bg-nutrition-blue hover:bg-nutrition-darkBlue focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-nutrition-yellow disabled:opacity-60 disabled:cursor-not-allowed"
            >
              {submitting ? "Enviando..." : "Enviar"}
              <span className="ml-2 text-lg">→</span>
            </button>
          </div>
        </form>
      </div>
    </LayoutGeneral>
  );
}

export default UserIntakeForm;