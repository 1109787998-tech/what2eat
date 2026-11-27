from fastapi import FastAPI
from src.dish.router import router

app = FastAPI(
    title = "What2Eat",
    version = "0.1.0",
    description = "菜品管理系统",
    )

app.include_router(router)