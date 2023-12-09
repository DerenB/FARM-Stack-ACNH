from fastapi import APIRouter, HTTPException
from models.bug_model import BugModel

# Create Router
router = APIRouter()

# Import Database Functions
from database_functions.bug_db_functions import (
    read_all_bugs,
    read_bugs_by_name
)


# Read All Bugs
@router.get("/bugs", tags=["bugs"])
async def get_all_bugs():
    response = await read_all_bugs()
    return response


# Read Bugs by Title
@router.get("/bugs/{title}", tags=["bugs"])
async def get_bugs_by_title(title):
    response = await read_bugs_by_name(title)
    if response:
        return response
    raise HTTPException(404, f"There are no bugs with this title: {title}")