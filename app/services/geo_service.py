import requests
from app.exceptions.exceptions import LocationNotFoundError, ProviderAPIError, ProviderSchemaError


def locate_city(city_name: str) -> tuple[float, float]:
    url = "https://geocoding-api.open-meteo.com/v1/search"

    query_params = {
        "name": city_name,
        "count": 1,
        "language":"pt",
        "format":"json"
    }

    try:
        response = requests.get(url, params=query_params, timeout=5)

        if response.status_code == 200:
            results = response.json().get("results")

            if results:
                geolocation = results[0]

                latitude = geolocation.get("latitude")
                longitude = geolocation.get("longitude")

                if latitude is None or longitude is None:
                    raise ProviderSchemaError("Geolocation Service", "SchemaNotFound")

                return latitude, longitude
            else:
                raise LocationNotFoundError(city_name)
        else:
            raise ProviderAPIError("Geolocation Service", response.status_code, f"Unable to reach Geolocation API")

    except requests.exceptions.ConnectionError as conn_err:
        raise ProviderAPIError("Geolocation Service", 502, f"{str(conn_err)}")
    except requests.exceptions.Timeout as timeout_err:
        raise ProviderAPIError("Geolocation Service", 504, f"{str(timeout_err)}")
    except requests.exceptions.RequestException as err:
        raise ProviderAPIError("Geolocation Service", 502, f"{str(err)}")

