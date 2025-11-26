import { request } from "./client";

// userInput debe seguir el esquema UserInput del backend
export async function generateDiet(userInput) {
  return await request("/diet/diet/generate", {
    method: "POST",
    body: JSON.stringify(userInput),
  });
}