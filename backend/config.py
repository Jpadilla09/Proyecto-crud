import mysql.connector
from mysql.connector import Error


class DatabaseConfig:
    # IMPORTANTE: cambia estos datos por los de TU MySQL
    HOST = 'localhost'
    PORT = 3307            # <-- puerto de MySQL en tu XAMPP
    USER = 'root'
    PASSWORD = ''          # <-- pon aquí tu contraseña de MySQL (vacía si no tiene, como en XAMPP)
    DATABASE = 'universidad_db'

    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host=DatabaseConfig.HOST,
                port=DatabaseConfig.PORT,
                user=DatabaseConfig.USER,
                password=DatabaseConfig.PASSWORD,
                database=DatabaseConfig.DATABASE
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None
