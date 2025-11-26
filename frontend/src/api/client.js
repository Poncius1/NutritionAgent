const BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

async function request(path, options = {}) {
  const url = `${BASE_URL}${path}`;

  const defaultHeaders = {
    "Content-Type": "application/json",
  };

  const config = {
    headers: { ...defaultHeaders, ...(options.headers || {}) },
    ...options,
  };

  const response = await fetch(url, config);

  let data;
  try {
    data = await response.json();
  } catch (e) {
    data = null;
  }

  if (!response.ok) {
    const msg =
      data?.detail ||
      data?.message ||
      (Array.isArray(data) && data[0]?.msg) || // típico de errores 422
      `Error ${response.status}`;
    console.error("Error en request:", response.status, data);
    throw new Error(msg);
  }

  return data;
}

export { request, BASE_URL };