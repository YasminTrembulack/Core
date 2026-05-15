from fastapi import FastAPI
from routes.user_route import router as user_route
from routes.health_route import router as health_route

app = FastAPI()

app.include_router(user_route)
app.include_router(health_route)