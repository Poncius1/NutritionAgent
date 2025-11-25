import { useState } from "react";

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

    // Validaciones básicas en front
    const age = Number(values.age);
    const weight = Number(values.weight);
    const height = Number(values.height);
    const fat = values.fat_percentage ? Number(values.fat_percentage) : null;

    if (isNaN(age) || age < 10 || age > 120) {
      alert("La edad debe estar entre 10 y 120 años.");
      setSubmitting(false);
      return false;
    }
    if (isNaN(weight) || weight <= 0) {
      alert("El peso debe ser mayor a 0 kg.");
      setSubmitting(false);
      return false;
    }
    if (isNaN(height) || height <= 0) {
      alert("La estatura debe ser mayor a 0.");
      setSubmitting(false);
      return false;
    }
    if (fat !== null && (fat < 1 || fat > 60)) {
      alert("El porcentaje de grasa corporal debe estar entre 1 y 60.");
      setSubmitting(false);
      return false;
    }

    const payload = {
      name: values.name,
      age,
      sex: values.sex, // "male" | "female"
      weight,
      height,
      fat_percentage: fat === null ? undefined : fat,
      exercise: values.exercise, // "0-1" | "2-3" | ...
      condition: values.condition, // "none" | "diabetes" | ...
      allergies: values.allergies
        ? values.allergies
            .split(",")
            .map((s) => s.trim())
            .filter(Boolean)
        : [],
    };

    try {
      // Cambia la URL por la de tu backend real
      const res = await fetch("http://localhost:8000/tu-endpoint", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        throw new Error("Error al enviar datos");
      }

      const data = await res.json();
      console.log("Respuesta del backend:", data);

      return true;
    } catch (err) {
      console.error(err);
      alert("Ocurrió un error al enviar el formulario");
      return false;
    } finally {
      setSubmitting(false);
    }
  }

  return { values, handleChange, handleSubmit, submitting };
}