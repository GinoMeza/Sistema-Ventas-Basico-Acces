import pyodbc

# Ruta a la base de datos Access
DB_PATH = r"database/reservas_agencia.accdb"

# Configuración de conexión
def conectar_db():
    conn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={DB_PATH};"
    )
    return conn
