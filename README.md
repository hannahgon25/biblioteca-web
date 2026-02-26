# Biblioteca Web

## Tecnologías

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Base de datos:** PostgreSQL
- **Contenedores:** Docker

---

##  Instrucciones

###  Base de datos

```bash
docker compose up -d
```

---

###  Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # En Linux
pip install flask psycopg2
python app.py
```

---

###  Frontend

Abrir `buscar.html` en el navegador.