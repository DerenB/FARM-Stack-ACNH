from pydantic import BaseModel

class BugModel(BaseModel):
    name: str
    icon: str
    selPrice: int
    weather: str
    location: str
    northTimeStart: int
    northTimeEnd: int
    southTimeStart: int
    southTimeEnd: int
    northMonthStart: int
    northMonthEnd: int
    southMonthStart: int
    southMonthEnd: int
    nMonthStartName: str
    nMonthEndName: str
    sMonthStartName: str