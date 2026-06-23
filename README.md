# SkyQuery

REST API built with FastAPI that provides astronomical information about a city, including sunrise, sunset and day length.

## About
SkyQuery was built as a study project to practice software engineering and backend development concepts, including:

- REST APIs
- FastAPI
- Pydantic
- SQLite
- External API integration
- Exception handling
- Software architecture

## Features

- Sunrise information
- Sunset information
- Day length calculation
- Search history persistence
- SQLite database
- Interactive Swagger documentation
- Error handling

## Architecture
The project follows a layered architecture:

- routes: HTTP endpoints
- services: business logic
- database: persistence layer
- schemas: Pydantic models
- exceptions: custom exceptions

## Technologies

- Python
- FastAPI
- Pydantic
- SQLite
- Requests
- Open-Meteo API

## Running Locally

Clone the repository:

```bash
git clone https://github.com/pedrolnog/SkyQuery.git
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run:
```bash
uvicorn app.main:app --reload
```
Then access:
```bash
http://127.0.0.1:8000
```

## API Documentation
Swagger documentation is available at:
```
http://localhost:8000/docs
```

<img width="1580" height="866" alt="image" src="https://github.com/user-attachments/assets/ccc481f5-8d5c-47fd-b691-91ec770e4cd0" />

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /astronomy?city=XXXXX | Returns astronomical data about a specified city. |
| GET | /astronomy/history | Returns the entire search history. |
| GET | /astronomy/history?city=XXXXX | Returns the search history for a specified city. |

### Example

```
GET /astronomy?city=London
```

Response:
```json
{
  "city": "London",
  "sunrise": "04:43",
  "sunset": "21:17",
  "day_length": {
    "formatted": "16h 34m",
    "seconds": 59640
  }
}
```

## Roadmap

### Current Version (v0.2)

- [x] FastAPI API
- [x] Pydantic models
- [x] SQLite persistence
- [x] Search history
- [x] Swagger documentation

### Future Improvements

- [ ] Async requests with httpx
- [ ] Unit tests
- [ ] Moon phase calculations
- [ ] Moon illumination
- [ ] Local astronomical calculations with Astropy
