from fastapi import APIRouter, HTTPException

# Create Router
router = APIRouter()

# Read All Bugs
@router.get("/")
async def get_all_bugs():
    return {"location": "Home Page"}