# Flask Superheroes API

## Description
This project is a Flask API for tracking heroes and their superpowers. It allows you to manage heroes, powers, and the relationships between them, including the strength of each hero's power.

## Features
- Manage heroes and their superpowers
- Many-to-many relationship between heroes and powers through HeroPower
- Validations on power descriptions and hero power strength
- RESTful API endpoints for CRUD operations
- Database migrations and seeding for initial data

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Seed the database with initial data:
   ```
   python seed.py
   ```

6. Run the Flask server:
   ```
   python app.py
   ```

The server will run on `http://localhost:5555`.

## API Endpoints

- `GET /heroes` - List all heroes
- `GET /heroes/<id>` - Get details of a specific hero including their powers
- `GET /powers` - List all powers
- `GET /powers/<id>` - Get details of a specific power
- `PATCH /powers/<id>` - Update a power's description
- `POST /hero_powers` - Create a new hero power association

## Validations

- `HeroPower.strength` must be one of: `Strong`, `Weak`, `Average`
- `Power.description` must be present and at least 20 characters long

## Testing

You can test the API endpoints using tools like curl or Postman. The provided Postman collection `challenge-2-superheroes.postman_collection.json` contains all the endpoints for easy import and testing.

## License

This project is licensed under the MIT License.

## Author

Marvin Daniel


