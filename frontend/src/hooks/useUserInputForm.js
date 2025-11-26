import { useState } from "react";
import { generateDiet } from "../api/diet";

const initialValues = {
  name: "",
  age: "",
  sex: "male",
  weight: "",
  height: "",
  fat_percentage: "",
  exercise: "0-1",
  condition: "none",
  allergies: "",
};

export function useUserInputForm() {
  const [values, setValues] = useState(initialValues);
  const [submitting, setSubmitting] = useState(false);

  function handleChange(field) {
    return (eventOrValue) => {
      const value =
        typeof eventOrValue === "string"
          ? eventOrValue
          : eventOrValue.target.value;

      setValues((prev) => ({
        ...prev,
        [field]: value,
      }));
    };
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setSubmitting(true);

    const age = Number(values.age);
    const weight = Number(values.weight);
    const height = Number(values.height);
    const fat = values.fat_percentage ? Number(values.fat_percentage) : null;

    if (isNaN(age) || age < 10 || age > 120) {
      alert("La edad debe estar entre 10 y 120 años.");
      setSubmitting(false);
      return null;
    }
    if (isNaN(weight) || weight <= 0) {
      alert("El peso debe ser mayor a 0 kg.");
      setSubmitting(false);
      return null;
    }
    if (isNaN(height) || height <= 0) {
      alert("La estatura debe ser mayor a 0.");
      setSubmitting(false);
      return null;
    }
    if (fat !== null && (fat < 1 || fat > 60)) {
      alert("El porcentaje de grasa corporal debe estar entre 1 y 60.");
      setSubmitting(false);
      return null;
    }

    const payload = {
      name: values.name,
      age,
      sex: values.sex,
      weight,
      height,
      fat_percentage: fat === null ? undefined : fat,
      exercise: values.exercise,
      condition: values.condition,
      allergies: values.allergies
        ? values.allergies
            .split(",")
            .map((s) => s.trim())
            .filter(Boolean)
        : [],
    };

    try {
      const result = await generateDiet(payload);
      console.log("Respuesta /diet/diet/generate:", result);
      // devolvemos el resultado para que lo use la página
      return result;
    } catch (err) {
      console.error("Error al generar dieta:", err);
      alert(err.message || "Ocurrió un error al enviar el formulario.");
      return null;
    } finally {
      setSubmitting(false);
    }
  }

  return { values, handleChange, handleSubmit, submitting };
}