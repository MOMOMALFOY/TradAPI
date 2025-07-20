import os
from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from langdetect import detect
from deep_translator import GoogleTranslator
from typing import Optional

# Pour Railway : récupérer le port depuis la variable d'environnement
PORT = int(os.environ.get("PORT", 8000))  # Utilisé seulement si tu lances via Python directement

app = FastAPI(
    title="Detection & Traduction Langue API",
    description="API de détection et traduction de langue, utilisable uniquement via RapidAPI.",
    version="1.0.0"
)

# Vérification proxy RapidAPI (comme RestCountriesAPI)
async def verify_rapidapi_proxy(request: Request):
    if not (request.headers.get("x-rapidapi-host") or request.headers.get("x-rapidapi-user")):
        raise HTTPException(status_code=401, detail="Accès uniquement via le proxy RapidAPI.")

class TextRequest(BaseModel):
    text: str

class TranslateRequest(BaseModel):
    text: str
    target: str

@app.get("/", tags=["Accueil"])
async def accueil():
    return {
        "message": "Bienvenue sur l'API de détection et traduction de langue. Utilisez cette API via RapidAPI (header x-rapidapi-host obligatoire). Consultez la documentation RapidAPI pour les exemples."
    }

@app.get("/ping", tags=["Healthcheck"])
async def ping():
    return {"status": "ok"}

@app.post("/detect", tags=["Détection"])
async def detect_lang_post(request: Request, data: TextRequest):
    await verify_rapidapi_proxy(request)
    try:
        lang = detect(data.text)
        return {"lang": lang}
    except Exception as e:
        return {"error": str(e)}

@app.get("/detect", tags=["Détection"])
async def detect_lang_get(request: Request, text: str = Query(..., description="Texte à détecter")):
    await verify_rapidapi_proxy(request)
    try:
        lang = detect(text)
        return {"lang": lang}
    except Exception as e:
        return {"error": str(e)}

@app.post("/translate", tags=["Traduction"])
async def translate_text_post(request: Request, data: TranslateRequest):
    await verify_rapidapi_proxy(request)
    try:
        translated = GoogleTranslator(target=data.target).translate(data.text)
        return {"translated": translated}
    except Exception as e:
        return {"error": str(e)}

@app.get("/translate", tags=["Traduction"])
async def translate_text_get(
    request: Request,
    text: str = Query(..., description="Texte à traduire"),
    target: str = Query(..., description="Langue cible (ex: 'en', 'fr', 'es')")
):
    await verify_rapidapi_proxy(request)
    try:
        translated = GoogleTranslator(target=target).translate(text)
        return {"translated": translated}
    except Exception as e:
        return {"error": str(e)}

@app.post("/detect-translate", tags=["Détection+Traduction"])
async def detect_and_translate_post(request: Request, data: TranslateRequest):
    await verify_rapidapi_proxy(request)
    try:
        detected_lang = detect(data.text)
        translated = GoogleTranslator(source=detected_lang, target=data.target).translate(data.text)
        return {"detected": detected_lang, "translated": translated}
    except Exception as e:
        return {"error": str(e)}

@app.get("/detect-translate", tags=["Détection+Traduction"])
async def detect_and_translate_get(
    request: Request,
    text: str = Query(..., description="Texte à détecter et traduire"),
    target: str = Query(..., description="Langue cible (ex: 'en', 'fr', 'es')")
):
    await verify_rapidapi_proxy(request)
    try:
        detected_lang = detect(text)
        translated = GoogleTranslator(source=detected_lang, target=target).translate(text)
        return {"detected": detected_lang, "translated": translated}
    except Exception as e:
        return {"error": str(e)}

# ---
# Exemple de commande Railway (dans le Procfile ou Start Command) :
# uvicorn main:app --host 0.0.0.0 --port $PORT
# --- 