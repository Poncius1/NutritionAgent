/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        nutrition: {
          darkBlue: "#1a3f5f",
          blue: "#20639b",
          teal: "#3caea3",
          yellow: "#f6d55c",
          orange: "#ed553b",
        },
      },
      borderRadius: {
        card: "1.5rem",
      },
      boxShadow: {
        card: "0 18px 40px rgba(0, 0, 0, 0.12)",
      },
    },
  },
  plugins: [],
};