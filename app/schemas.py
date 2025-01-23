from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    lat: float
    lon: float
    excluded_types: list[str] = []
