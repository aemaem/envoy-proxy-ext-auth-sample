import os

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

path_prefix = os.getenv("PATH_PREFIX", "")

app = FastAPI(openapi_url=f"{path_prefix}/openapi.json")


@app.get(f"{path_prefix}/")
async def index():
    return {
        "title": "The index page",
    }


@app.get(f"{path_prefix}/lenny")
async def lenny():
    return {
        "title": "Are You Gonna Go My Way",
        "interpret": "Lenny Kravitz",
        "lyrics": """I was born long ago
I am the chosen, I'm the one
I have come to save the day
And I won't leave until I'm done
So that's why you've got to try
You got to breath and have some fun
Though I'm not paid, I play this game
And I won't stop until I'm done
But what I really want to know is
Are you gonna go my way?
And I got to, got to know
I don't know why we always cry
This we must leave and get undone
We must engage and rearrange
And turn this planet back to one
So tell me why we got to die
And kill each other one by one
We've got to hug and rub-a-dub
We've got to dance and be in love
Are you gonna go my way?
And I got to, got to know
Are you gonna go my way?
'Cause, baby, I got to know
Yeah""",
    }


@app.get("/health")
async def health():
    return {"status": "UP"}


@app.on_event("startup")
async def startup():
    Instrumentator(excluded_handlers=["/metrics"], should_respect_env_var=True,
                   env_var_name="ENABLE_METRICS").instrument(app).expose(app)
