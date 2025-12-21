from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import joblib
import os
from datetime import datetime

app = FastAPI(
    title="Sentiment Analysis ML Service",
    description="API de Machine Learning para análisis de sentimientos",
    version="1.0.0"
)

# Modelo global (se carga al iniciar)
model = None
vectorizer = None

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    prevision: str
    probabilidad: float
    timestamp: str

@app.on_event("startup")
async def load_model():
    """Cargar modelo al iniciar la aplicación"""
    global model, vectorizer
    model_path = "../models/sentiment_model.pkl"
    
    if os.path.exists(model_path):
        try:
            data = joblib.load(model_path)
            model = data.get('model')
            vectorizer = data.get('vectorizer')
            print("✅ Modelo cargado correctamente")
        except Exception as e:
            print(f"❌ Error al cargar modelo: {e}")
    else:
        print(f"⚠️ Modelo no encontrado en {model_path}")

@app.get("/")
async def root():
    return {
        "message": "Sentiment Analysis ML Service",
        "version": "1.0.0",
        "status": "running",
        "model_loaded": model is not None
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy" if model is not None else "degraded",
        "model_loaded": model is not None,
        "timestamp": datetime.now().isoformat()
    }

@app.post("/predict", response_model=SentimentResponse)
async def predict(request: SentimentRequest):
    if model is None or vectorizer is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo no cargado"
        )
    
    try:
        # Vectorizar texto
        text_vectorized = vectorizer.transform([request.text])
        
        # Predecir
        prediction = model.predict(text_vectorized)[0]
        probabilities = model.predict_proba(text_vectorized)[0]
        
        # Obtener probabilidad de la clase predicha
        class_idx = list(model.classes_).index(prediction)
        probability = float(probabilities[class_idx])
        
        # Mapear a nombres
        sentiment_map = {0: "Negativo", 1: "Positivo"}
        sentiment = sentiment_map.get(prediction, "Desconocido")
        
        return SentimentResponse(
            prevision=sentiment,
            probabilidad=round(probability, 4),
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
