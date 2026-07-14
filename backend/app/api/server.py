from fastapi import FastAPI

app = FastAPI(
    title="OpenRoIP API",
    version="0.1.0",
    description="REST API for OpenRoIP"
)


@app.get("/")
def root():
    return {
        "application": "OpenRoIP",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
