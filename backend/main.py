from fastapi import FastAPI

from paths import (
    bug_routes
)

# Start App
app = FastAPI()

# App Routes
app.include_router(bug_routes.router)
