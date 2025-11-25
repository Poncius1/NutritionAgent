import { Routes, Route } from "react-router-dom";
import Welcome from "./pages/Welcome";
import UserIntakeForm from "./pages/UserIntakeForm";
import Success from "./pages/Success";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Welcome />} />
      <Route path="/intake" element={<UserIntakeForm />} />
      <Route path="/success" element={<Success />} />
    </Routes>
  );
}

export default App;