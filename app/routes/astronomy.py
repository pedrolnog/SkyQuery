from fastapi import APIRouter, HTTPException
from app.schemas.astronomy_models import AstronomyResponse
from app.database.models import HistoryModel
from app.database.connection import get_search_history
from app.exceptions.exceptions import ProviderAPIError, LocationNotFoundError, ProviderSchemaError
from app.services.astronomy_service import receive_astro_data

router = APIRouter()
@router.get("/astronomy", status_code=200, response_model=AstronomyResponse, summary="Returns astronomical data about a city.", description = "Returns information about a city's sunrise, sunset and day length based on its geographical coordinates.", tags=["Astronomy"])
def read_astro_info(city: str):
    try:
        astro_data = receive_astro_data(city)

        return astro_data

    except ProviderAPIError as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))

    except LocationNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except ProviderSchemaError as e:
        raise HTTPException(status_code=502, detail=str(e))

@router.get("/astronomy/history", status_code=200, response_model=list[HistoryModel], summary="Returns the search history of the API, with the option to search by city")
def read_history(city: str | None = None):
    if city:
        return get_search_history(city)
    else:
        return get_search_history()