from fastapi import FastAPI
from routes.astronomy import router
from contextlib import asynccontextmanager
from database.connection import get_connection, create_tables

@asynccontextmanager
async def lifespan(_: FastAPI):
    with get_connection() as connection:
        create_tables(connection)

    yield
app = FastAPI(
    title="Astronomy API",
    description="API for receiving astronomical data about a specific city.",
    version="0.2",
    lifespan=lifespan
)
app.include_router(router)
