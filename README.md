# Hackathon - Análisis de Sentimientos

API de Machine Learning diseñada para clasificar sentimientos en comentarios (Positivo/Negativo), permitiendo a las empresas automatizar la gestión de feedback y priorizar la atención al cliente.

# Arquitectura
El proyecto sigue una arquitectura de microservicios e integración híbrida: Frontend (React/HTML) → Backend (Spring Boot) → ML Service (FastAPI) → H2/PostgreSQL

## Estructura
hackathon-sentiment-analysis/
├── backend/          # API REST Spring Boot (Puerto 8080)
├── data-science/     # Modelo ML + API FastAPI (Puerto 8000)
├── frontend/         # Interfaz web React (Puerto 3000)
└── docs/            # Documentación y capturas

# Inicio Rápido

### Backend
```bash
cd backend
mvn spring-boot:run
```

### Data Science (ML Service)
```bash
cd data-science
source venv/bin/activate
cd api
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm start
```

## Endpoints

### ML Service (FastAPI) - http://localhost:8000
- `POST /predict` - Predecir sentimiento
- `GET /health` - Health check
- `GET /docs` - Documentación Swagger

### Backend API - http://localhost:8080
- `POST /api/sentiment` - Analizar sentimiento
- `GET /api/stats` - Estadísticas

## Equipo

- **Backend**: [Nombres]
- **Data Science**: [Nombres]
- **Frontend**: [Nombres]

## Git Workflow
```bash
# Trabajar en tu rama
git checkout feature/backend  # o tu rama

# Hacer cambios
git add .
git commit -m "feat: descripción"
git push origin feature/backend

# Crear Pull Request en GitHub
# feature/backend → develop
```

## Tecnologías Utilizadas

- Backend: Java 17, Spring Boot 3.x, Spring Data JPA, Spring Security 6.
- Data Science: Python 3.10, Scikit-learn, Pandas, FastAPI, Joblib.
- Database: H2 (Desarrollo) / PostgreSQL (Producción).
- Frontend: React 18, HTML5/JS (Fetch API).

---

#   Para Data Science
cd ~/hackathon-sentiment-analysis
git checkout feature/data-science
cd data-science
source venv/bin/activate
jupyter notebook
# Trabajar en notebooks/training.ipynb


#   Para Backend:
cd ~/hackathon-sentiment-analysis
git checkout feature/backend
cd backend
# Empezar a crear controllers, services, etc.


#   Para Frontend:
cd ~/hackathon-sentiment-analysis
git checkout feature/frontend
cd frontend
npx create-react-app .
