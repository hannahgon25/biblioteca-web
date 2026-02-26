# Biblioteca Web

## Tecnologías
Backend: Python (Flask)
Frontend: HTML, CSS, Javascript
Base de datos: PostgreSQL
Contenedores: Docker

## Instrucciones

### Base de datos
docker compose up -d

### Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install flask psycopg2
python app.py

### Frontend
Abrir buscar.html en el navegador