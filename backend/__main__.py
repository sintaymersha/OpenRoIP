import uvicorn

from app.core.startup import initialize


def main():
    initialize()

    uvicorn.run(
        "app.api.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
