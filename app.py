from fastapi import FastAPI
from routes.user_route import router as user_route
from routes.alarm_route import router as alarm_route
from routes.health_route import router as health_route
from routes.user_unit_route import router as user_unit_route
from config import settings

app = FastAPI()

app.include_router(user_route)
app.include_router(alarm_route)
app.include_router(health_route)
app.include_router(user_unit_route)


if __name__ == "__main__":
    import uvicorn

    port = int(settings.PORT)
    must_reload = settings.ENV == "development"

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=must_reload,
    )