# 🧠 Nutrition AI Agent

### Sistema Inteligente para la Generación de Recomendaciones Nutricionales Personalizadas

---

## 🚀 Descripción General

**Nutrition AI Agent** es una aplicación web que genera **recomendaciones nutricionales personalizadas** a partir de los datos de cada usuario.  
El sistema emplea **algoritmos evolutivos (Genéticos)** y **Recocido Simulado** combinados dentro de un **agente de búsqueda inteligente**, que optimiza los valores nutricionales según las necesidades del usuario.

El objetivo **no es generar menús diarios específicos**, sino ofrecer un **régimen nutricional ideal** (cantidad de proteínas, lípidos, carbohidratos, energía y agua) adaptado a características como edad, sexo, peso, condiciones médicas y nivel de actividad física.

---

## 🧩 Arquitectura del Proyecto

La estructura sigue un modelo **modular y escalable**, separando el backend (lógica de IA y cálculos) del frontend (interfaz de usuario).

```bash
📦 nutrition-ai-agent/
│
├── backend/                  # 🧠 API y agente de búsqueda (FastAPI)
│   ├── algorithms/           # Algoritmos genético y recocido simulado
│   ├── api/                  # Endpoints de la API
│   ├── data/                 # Fuente de datos (CSV de CONABIO)
│   ├── models/               # Modelos con Pydantic
│   ├── services/             # Lógica: filtros, cálculos y agente de búsqueda
│   ├── main.py               # Punto de entrada del servidor FastAPI
│   └── requirements.txt      # Dependencias del backend
│
├── frontend/                 # Interfaz de usuario (React)
│   ├── src/                  # Componentes, vistas y conexión con la API
│   ├── public/               # Archivos estáticos
│   ├── package.json          # Configuración de dependencias
│   └── ...
│
├── .gitignore              
└── README.md             

```

### 🐍 Backend — Python (FastAPI)

```bash
# 1️⃣ Entrar a la carpeta del backend
cd backend

# 2️⃣ Crear y activar el entorno virtual
python -m venv venv
# En Windows:
source venv/Scripts/activate
# En macOS/Linux:
source venv/bin/activate

# 3️⃣ Instalar dependencias
pip install -r requirements.txt

# 4️⃣ Ejecutar el servidor FastAPI
uvicorn main:app --reload

El servidor se ejecutará en:
👉 http://127.0.0.1:8000

```


### ⚛️ Frontend — JavaScript (React)
```bash
cd frontend
npm install
npm start

La interfaz se abrirá en:
👉 http://localhost:3000
```


