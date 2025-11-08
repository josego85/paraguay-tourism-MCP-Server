from pydantic import BaseModel

class Place(BaseModel):
    id: str
    name: str
    description: str
    category: str
    lat: float
    lng: float
    city: str
    region: str