# Conference Room Reservation API

A simple Flask API for managing conference room reservations.

## Features

- Create reservations for conference rooms
- List all reservations
- Delete reservations
- Validation: No overlapping reservations, no past reservations, start before end
- Data stored in memory (not persistent across restarts)

## Installation

1. Install Python 3.x if not already installed.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the API

Run the application:
```
python app.py
```

The API will start on `http://127.0.0.1:5000/`

## API Endpoints

### Create a Reservation
- **POST** `/reservations`
- **Body** (JSON):
  ```json
  {
    "room": "Room A",
    "start_time": "2026-01-20T10:00:00",
    "end_time": "2026-01-20T11:00:00",
    "user": "John Doe"
  }
  ```
- **Response**: `{"id": 1, "message": "Reservation created successfully"}`

### Get All Reservations
- **GET** `/reservations`
- **Response**: Array of reservations
  ```json
  [
    {
      "id": 1,
      "room": "Room A",
      "start_time": "2026-01-20T10:00:00",
      "end_time": "2026-01-20T11:00:00",
      "user": "John Doe"
    }
  ]
  ```

### Delete a Reservation
- **DELETE** `/reservations/<id>`
- **Response**: `{"message": "Reservation deleted successfully"}`

## Validation Rules

- Start time must be before end time
- Reservations cannot be made in the past
- Reservations for the same room cannot overlap

## Notes

- Data is stored in memory and will be lost when the server restarts.
- No database is used; all data is temporary.

## Troubleshooting

- Ensure all required fields are provided in POST requests.
- Use ISO 8601 format for datetime strings (e.g., `2026-01-20T10:00:00`).