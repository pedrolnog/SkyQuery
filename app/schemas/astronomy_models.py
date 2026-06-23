from pydantic import BaseModel, Field

class DayLength(BaseModel):
    """
    Information about the day's length.
    """
    formatted : str = Field(description="Formatted day length (HH:MM).")
    seconds: int = Field(description="Day's length in seconds.", examples=["59640", "41700"])

class AstronomyResponse(BaseModel):
    """
    Model for the API's response. It contains general astronomic data.
    """

    city: str = Field(description="Name of the searched city.", examples=["New York", "San Francisco"])
    sunrise: str = Field(description="Sunrise time in the city's timezone.", examples=["05:42", "06:00"])
    sunset: str = Field(description="Sunset time in the city's timezone.", examples=["17:41", "17:29"])
    day_length: DayLength
