from fastapi import FastAPI

from app.core.startup import initialize

from app.api.routes.system import router as system_router
from app.api.routes.radio import router as radio_router
from app.api.routes.audio import router as audio_router   


app = FastAPI(
    title="OpenRoIP API",
    version="0.1.0",
)


@app.on_event("startup")
def startup_event():
    initialize()


app.include_router(system_router)
app.include_router(radio_router)
app.include_router(audio_router)      


@app.get("/")
def root():
    return {
        "application": "OpenRoIP",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }