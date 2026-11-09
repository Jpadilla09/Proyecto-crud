# Taller APIs CRUD – Estudiantes (Flask + MySQL + HTML/JS)

Universidad Libre Seccional Pereira – Programación II, Sistemas Distribuidos.
Versión 1: Front – API – Backend – Persistencia.

## Estructura
```
proyecto-crud/
├── backend/
│   ├── app.py              # Aplicación principal (Flask + CORS)
│   ├── config.py           # Configuración de la base de datos
│   ├── models.py           # Modelo Estudiante y creación de tabla
│   ├── routes/estudiantes.py  # Rutas CRUD
│   ├── requirements.txt    # Dependencias
│   └── database.sql        # Script SQL inicial
├── frontend/
│   ├── index.html
│   ├── css/styles.css
│   └── js/app.js
└── evidencias/             # Capturas de las pruebas
```

## Cómo ejecutarlo
1. Iniciar MySQL (por ejemplo con XAMPP) y crear la base de datos ejecutando `backend/database.sql`.
2. Editar `backend/config.py` con tus credenciales y **tu puerto de MySQL**
   (`PORT = 3307` en mi equipo; el valor por defecto de MySQL es `3306`).
3. En la carpeta `backend`:
   ```
   python -m venv .venv
   .venv\Scripts\activate        (Windows)
   pip install -r requirements.txt
   python app.py
   ```
4. En la carpeta `frontend`:
   ```
   python -m http.server 8000
   ```
   y abrir http://localhost:8000

## Endpoints de la API
| Método | Ruta                   | Acción        |
|--------|------------------------|---------------|
| GET    | /api/estudiantes       | Listar todos  |
| GET    | /api/estudiantes/<id>  | Obtener uno   |
| POST   | /api/estudiantes       | Crear         |
| PUT    | /api/estudiantes/<id>  | Actualizar    |
| DELETE | /api/estudiantes/<id>  | Eliminar      |

## Evidencias
Las capturas de las pruebas del CRUD están en la carpeta `evidencias/`.
