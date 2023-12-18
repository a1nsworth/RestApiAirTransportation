from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from aviation_personnel.router import aviation_personnel_router
from available_cities.router import available_cities_router
from client.router import client_router

app = FastAPI()

app.include_router(router=aviation_personnel_router)
app.include_router(router=available_cities_router)
app.include_router(router=client_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
