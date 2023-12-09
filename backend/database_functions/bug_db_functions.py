from models.bug_model import BugModel
from dotenv import load_dotenv
import os
# Import Items

# Load Secret Connection String
load_dotenv()
connection_string = os.getenv("ConnectionString")

# MongoDB Driver
import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)

# Create Database & Collection
database = client.ACNHFarmDeploy
collection = database.bugs


# Read All Bugs
async def read_all_bugs():
    bug_list = []
    cursor = collection.find({})
    async for document in cursor:
        bug_list.append(BugModel(**document))
    return bug_list


# Query Bugs by Name
async def read_bugs_by_name(title):
    bug_list = []
    regex_expression = ".*" + title.lower() + ".*"
    query = { "name": { "$regex": regex_expression } }
    print(query)
    cursor = collection.find({"name": {"$regex": regex_expression}})
    async for document in cursor:
        bug_list.append(BugModel(**document))
    return bug_list
