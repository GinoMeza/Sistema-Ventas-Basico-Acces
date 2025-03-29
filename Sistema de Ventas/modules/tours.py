from database.db_config import conectar_db

def agregar_tour(nombre, descripcion, precio, cupos):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Tours (Nombre, Descripcion, Precio, Cupos_Disponibles)
        VALUES (?, ?, ?, ?)
    """, (nombre, descripcion, precio, cupos))
    conn.commit()
    conn.close()
    print("Tour agregado correctamente.")
