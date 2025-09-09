# Products Application

A full-stack application with React frontend and FastAPI backend.

## Project Structure

```
├── frontend/          # React frontend application
│   ├── src/          # React source code
│   ├── public/       # Static assets
│   └── package.json  # Frontend dependencies
├── backend/          # FastAPI backend application
│   ├── main.py       # FastAPI application
│   └── requirements.txt # Backend dependencies
└── README.md         # This file
```

## Getting Started

### Frontend (React)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

### Backend (FastAPI)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install python3-venv if not already installed (Ubuntu/Debian):
```bash
sudo apt install python3.10-venv
```

3. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Start the development server:
```bash
python main.py
```

The backend will be available at `http://localhost:8000`

## Development

- Frontend runs on port 3000
- Backend runs on port 8000
- CORS is configured to allow frontend-backend communication
         