from flask import Blueprint, jsonify, request
from config import DatabaseConfig

estudiantes_bp = Blueprint('estudiantes', __name__)

CAMPOS = ['nombre', 'apellido', 'edad', 'carrera']


def datos_validos(data):
    """Verifica que el JSON traiga todos los campos."""
    return data is not None and all(c in data and str(data[c]).strip() != '' for c in CAMPOS)


# CREATE - Crear estudiante
@estudiantes_bp.route('/api/estudiantes', methods=['POST'])
def crear_estudiante():
    data = request.get_json(silent=True)
    if not datos_validos(data):
        return jsonify({'error': 'Faltan datos: nombre, apellido, edad y carrera son obligatorios'}), 400

    connection = DatabaseConfig.get_connection()

    if connection:
        cursor = connection.cursor()
        query = """INSERT INTO estudiantes (nombre, apellido, edad, carrera)
                   VALUES (%s, %s, %s, %s)"""
        valores = (data['nombre'], data['apellido'], data['edad'], data['carrera'])

        cursor.execute(query, valores)
        connection.commit()

        nuevo_id = cursor.lastrowid
        cursor.close()
        connection.close()

        return jsonify({
            'mensaje': 'Estudiante creado exitosamente',
            'id': nuevo_id
        }), 201

    return jsonify({'error': 'Error de conexión'}), 500


# READ - Obtener todos los estudiantes
@estudiantes_bp.route('/api/estudiantes', methods=['GET'])
def obtener_estudiantes():
    connection = DatabaseConfig.get_connection()

    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estudiantes")
        estudiantes = cursor.fetchall()
        cursor.close()
        connection.close()

        return jsonify(estudiantes), 200

    return jsonify({'error': 'Error de conexión'}), 500


# READ - Obtener un estudiante por ID
@estudiantes_bp.route('/api/estudiantes/<int:id>', methods=['GET'])
def obtener_estudiante(id):
    connection = DatabaseConfig.get_connection()

    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id,))
        estudiante = cursor.fetchone()
        cursor.close()
        connection.close()

        if estudiante:
            return jsonify(estudiante), 200
        return jsonify({'error': 'Estudiante no encontrado'}), 404

    return jsonify({'error': 'Error de conexión'}), 500


# UPDATE - Actualizar estudiante
@estudiantes_bp.route('/api/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    data = request.get_json(silent=True)
    if not datos_validos(data):
        return jsonify({'error': 'Faltan datos: nombre, apellido, edad y carrera son obligatorios'}), 400

    connection = DatabaseConfig.get_connection()

    if connection:
        cursor = connection.cursor()
        query = """UPDATE estudiantes
                   SET nombre=%s, apellido=%s, edad=%s, carrera=%s
                   WHERE id=%s"""
        valores = (data['nombre'], data['apellido'], data['edad'],
                   data['carrera'], id)

        cursor.execute(query, valores)
        connection.commit()

        filas_afectadas = cursor.rowcount   # se lee ANTES de cerrar el cursor
        cursor.close()
        connection.close()

        if filas_afectadas > 0:
            return jsonify({'mensaje': 'Estudiante actualizado exitosamente'}), 200
        return jsonify({'error': 'Estudiante no encontrado'}), 404

    return jsonify({'error': 'Error de conexión'}), 500


# DELETE - Eliminar estudiante
@estudiantes_bp.route('/api/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    connection = DatabaseConfig.get_connection()

    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id = %s", (id,))
        connection.commit()

        filas_afectadas = cursor.rowcount   # se lee ANTES de cerrar el cursor
        cursor.close()
        connection.close()

        if filas_afectadas > 0:
            return jsonify({'mensaje': 'Estudiante eliminado exitosamente'}), 200
        return jsonify({'error': 'Estudiante no encontrado'}), 404

    return jsonify({'error': 'Error de conexión'}), 500
