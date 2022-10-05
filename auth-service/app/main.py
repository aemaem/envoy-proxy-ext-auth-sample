import os

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from prometheus_fastapi_instrumentator import Instrumentator

path_prefix = os.getenv("PATH_PREFIX", "")

app = FastAPI(openapi_url=f"{path_prefix}/openapi.json")
security = HTTPBasic()


@app.get(f"{path_prefix}/authenticate")
async def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == "admin" and credentials.password == "admin":
        return {"message": "Successfully authenticated"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect email or password",
        headers={"WWW-Authenticate": "Basic"},
    )


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.on_event("startup")
async def startup():
    Instrumentator(excluded_handlers=["/metrics"], should_respect_env_var=True,
                   env_var_name="ENABLE_METRICS").instrument(app).expose(app)
