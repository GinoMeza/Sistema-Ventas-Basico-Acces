from database.db_config import conectar_db

def agregar_reserva(ID_Cliente, ID_Tour, Fecha_Reserva, Cantidad):
    conn = conectar_db()
    cursor = conn.cursor()

    try:
        # Verificar si el tour existe y obtener su precio
        cursor.execute("SELECT Precio FROM Tours WHERE ID_Tour = ?", (ID_Tour,))
        tour_data = cursor.fetchone()

        if tour_data is None:
            print("Error: El tour con el ID proporcionado no existe.")
            return

        precio_tour = tour_data[0]  # Obtener el precio del tour

        # Calcular el total
        Total = precio_tour * Cantidad

        # Insertar la reserva en la tabla Reservas
        cursor.execute("""
            INSERT INTO Reservas (ID_Cliente, ID_Tour, Fecha_Reserva, Cantidad, Total)
            VALUES (?, ?, ?, ?, ?)
        """, (ID_Cliente, ID_Tour, Fecha_Reserva, Cantidad, Total))  # Los parámetros coinciden con los ?

        # Confirmar los cambios
        conn.commit()
        print("Reserva agregada correctamente.")

    except Exception as e:
        print(f"Error al agregar la reserva: {e}")

    finally:
        conn.close()
