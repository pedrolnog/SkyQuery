class LocationNotFoundError(Exception):
    def __init__(self, location_query: str):
        self.location_query = location_query
        super().__init__(f"Unable to locate the term: {location_query}.")

class ProviderAPIError(Exception):
    def __init__(self, provider_name: str, status_code: int, details: str):
        self.provider_name = provider_name
        self.status_code = status_code
        self.details = details
        super().__init__(f"{self.provider_name} returned {status_code}: {details}.")

class ProviderSchemaError(Exception):
    def __init__(self, provider_name: str, error):
        self.provider_name = provider_name
        self.error = error
        super().__init__(f"{provider_name} failed to return expected data: {error}.")

