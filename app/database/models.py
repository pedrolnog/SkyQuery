from pydantic import BaseModel, Field

class HistoryModel(BaseModel):
    """"
    Model for the history table.
    """
    id: int = Field(description="ID for the database entry", examples=[1, 1234])
    city: str = Field(description="Name of the city", examples=["New York", "São Paulo"])
    sunrise: str = Field(description="Sunrise time in the city's timezone.", examples=["05:42", "06:00"])
    sunset: str = Field(description="Sunset time in the city's timezone.", examples=["17:41", "17:29"])
    day_length_seconds: int = Field(description="Day's length in seconds.", examples=["59640", "41700"])
    search_time: str = Field(description="Search time", examples=['2026-06-18 18:12:49.523964', "2026-06-22 22:12:23.843409"])