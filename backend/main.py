from fastapi import FastAPI

from paths import (
    bug_routes,
    home
)

# Start App
app = FastAPI()

# App Routes
app.include_router(bug_routes.router)
app.include_router(home.router)
