from database.db_config import conectar_db

def agregar_cliente(nombres, apellidos, telefono, correo, direccion):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Clientes (Nombres, Apellidos, Telefono, Correo, Direccion)
        VALUES (?, ?, ?, ?, ?)
    """, (nombres, apellidos, telefono, correo, direccion))
    conn.commit()
    conn.close()
    print("Cliente agregado correctamente.")
