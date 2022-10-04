import os

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

path_prefix = os.getenv("PATH_PREFIX", "")

app = FastAPI(openapi_url=f"{path_prefix}/openapi.json")


@app.get(f"{path_prefix}/")
async def authenticate():
    # todo: authenticate user
    return {"message": "Successfully authenticated"}


@app.get(f"{path_prefix}/authenticate")
async def authenticate():
    # todo: authenticate user
    return {"message": "Successfully authenticated"}


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.on_event("startup")
async def startup():
    Instrumentator(excluded_handlers=["/metrics"], should_respect_env_var=True,
                   env_var_name="ENABLE_METRICS").instrument(app).expose(app)
