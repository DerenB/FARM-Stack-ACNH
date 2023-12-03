from fastapi import APIRouter, HTTPException
from models.bug_model import BugModel

# Create Router
router = APIRouter()

# Import Database Functions
from database_functions.bug_db_functions import (
    read_all_bugs
)


# Read All Bugs
@router.get("/bugs", tags=["bugs"])
async def get_all_bugs():
    response = await read_all_bugs()
    return response