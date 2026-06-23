import requests
import datetime as dt
from app.schemas.astronomy_models import DayLength, AstronomyResponse
from app.services.geo_service import locate_city
from app.database.connection import save_search
from app.exceptions.exceptions import ProviderSchemaError, ProviderAPIError

def calculate_day_length(sunrise: dt.datetime, sunset: dt.datetime) -> DayLength:
    day_length_seconds = int((sunset - sunrise).total_seconds())

    day_length_hours = int(day_length_seconds / 3600)
    day_length_minutes = int((day_length_seconds%3600) / 60)

    day_length = DayLength(formatted=f"{day_length_hours}h {day_length_minutes}m", seconds=day_length_seconds)

    return day_length

def receive_astro_data(city: str) -> AstronomyResponse:
    latitude, longitude = locate_city(city)

    url = "https://api.open-meteo.com/v1/forecast"
    query_params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["sunrise", "sunset"],
        "timezone": "auto",
        "forecast_days": "1",
    }

    try:
        response = requests.get(url, params=query_params, timeout=5)

        if response.status_code == 200:
            astro_data = response.json().get("daily")

            if astro_data:

                sunrise_raw = astro_data["sunrise"][0]
                sunset_raw = astro_data["sunset"][0]

                sunrise_dt = dt.datetime.fromisoformat(sunrise_raw)
                sunset_dt = dt.datetime.fromisoformat(sunset_raw)

                day_length = calculate_day_length(sunrise_dt, sunset_dt)

                astro_data = AstronomyResponse(
                    city=city.title(),
                    sunrise=sunrise_dt.strftime("%H:%M"),
                    sunset=sunset_dt.strftime("%H:%M"),
                    day_length=day_length
                )

                save_search(city, astro_data.sunrise, astro_data.sunset, astro_data.day_length.seconds)

                return astro_data

            else:
                raise ProviderSchemaError("Astronomy Service", "SchemaNotFound")
        else:
            raise ProviderAPIError("Astronomy Service", response.status_code, f"Unable to reach Astronomy Service")

    except requests.exceptions.ConnectionError as conn_err:
        raise ProviderAPIError("Astronomy Service", 502, f"Connection error occurred: {str(conn_err)}")
    except requests.exceptions.Timeout as timeout_err:
        raise ProviderAPIError("Astronomy Service", 504, f"Timeout error occurred: {str(timeout_err)}")
    except requests.exceptions.RequestException as err:
        raise ProviderAPIError("Astronomy Service", 502, f"Unable to reach Astronomy API: {str(err)}")
    except (TypeError, ValueError, KeyError) as err:
        raise ProviderSchemaError("Astronomy Service", err)
