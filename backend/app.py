from flask import Flask
from flask_cors import CORS
from routes.estudiantes import estudiantes_bp
from models import Estudiante

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

# Registrar blueprints (rutas)
app.register_blueprint(estudiantes_bp)


@app.route('/')
def index():
    return {'mensaje': 'API de Estudiantes - Universidad Libre'}, 200


if __name__ == '__main__':
    # Crear tabla al iniciar
    Estudiante.crear_tabla()
    print("Servidor iniciado en http://localhost:5000")
    app.run(debug=True, port=5000)
