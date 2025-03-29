import tkinter as tk
from tkinter import messagebox
from database.db_config import conectar_db
from modules.clientes import agregar_cliente
from modules.tours import agregar_tour
from modules.reservas import agregar_reserva

# Ventana para gestión de clientes
def gestion_clientes():
    def agregar():
        nombres = entry_nombres.get()
        apellidos = entry_apellidos.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        direccion = entry_direccion.get()
        
        if nombres and apellidos and telefono and correo and direccion:
            try:
                agregar_cliente(nombres, apellidos, telefono, correo, direccion)
                messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
                entry_nombres.delete(0, tk.END)
                entry_apellidos.delete(0, tk.END)
                entry_telefono.delete(0, tk.END)
                entry_correo.delete(0, tk.END)
                entry_direccion.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el cliente: {e}")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")

    ventana_clientes = tk.Toplevel()
    ventana_clientes.title("Gestión de Clientes")
    ventana_clientes.geometry("400x300")

    tk.Label(ventana_clientes, text="Nombres:").pack(pady=5)
    entry_nombres = tk.Entry(ventana_clientes)
    entry_nombres.pack()

    tk.Label(ventana_clientes, text="Apellidos:").pack(pady=5)
    entry_apellidos = tk.Entry(ventana_clientes)
    entry_apellidos.pack()

    tk.Label(ventana_clientes, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(ventana_clientes)
    entry_telefono.pack()

    tk.Label(ventana_clientes, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana_clientes)
    entry_correo.pack()

    tk.Label(ventana_clientes, text="Dirección:").pack(pady=5)
    entry_direccion = tk.Entry(ventana_clientes)
    entry_direccion.pack()

    tk.Button(ventana_clientes, text="Agregar Cliente", command=agregar).pack(pady=20)

# Ventana para gestión de tours
def gestion_tours():
    def agregar():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        precio = entry_precio.get()
        cupos = entry_cupos.get()

        if nombre and descripcion and precio and cupos:
            try:
                agregar_tour(nombre, descripcion, float(precio), int(cupos))
                messagebox.showinfo("Éxito", "Tour agregado correctamente.")
                entry_nombre.delete(0, tk.END)
                entry_descripcion.delete(0, tk.END)
                entry_precio.delete(0, tk.END)
                entry_cupos.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el tour: {e}")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")

    ventana_tours = tk.Toplevel()
    ventana_tours.title("Gestión de Tours")
    ventana_tours.geometry("400x300")

    tk.Label(ventana_tours, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana_tours)
    entry_nombre.pack()

    tk.Label(ventana_tours, text="Descripción:").pack(pady=5)
    entry_descripcion = tk.Entry(ventana_tours)
    entry_descripcion.pack()

    tk.Label(ventana_tours, text="Precio:").pack(pady=5)
    entry_precio = tk.Entry(ventana_tours)
    entry_precio.pack()

    tk.Label(ventana_tours, text="Cupos Disponibles:").pack(pady=5)
    entry_cupos = tk.Entry(ventana_tours)
    entry_cupos.pack()

    tk.Button(ventana_tours, text="Agregar Tour", command=agregar).pack(pady=20)

# Ventana para gestión de reservas
def gestion_reservas():
    def agregar():
        id_cliente = entry_id_cliente.get()
        id_tour = entry_id_tour.get()
        fecha_reserva = entry_fecha.get()
        cantidad = entry_cantidad.get()

        if id_cliente and id_tour and fecha_reserva and cantidad:
            try:
                agregar_reserva(int(id_cliente), int(id_tour), fecha_reserva, int(cantidad))
                messagebox.showinfo("Éxito", "Reserva agregada correctamente.")
                entry_id_cliente.delete(0, tk.END)
                entry_id_tour.delete(0, tk.END)
                entry_fecha.delete(0, tk.END)
                entry_cantidad.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar la reserva: {e}")
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")

    ventana_reservas = tk.Toplevel()
    ventana_reservas.title("Gestión de Reservas")
    ventana_reservas.geometry("400x300")

    tk.Label(ventana_reservas, text="ID Cliente:").pack(pady=5)
    entry_id_cliente = tk.Entry(ventana_reservas)
    entry_id_cliente.pack()

    tk.Label(ventana_reservas, text="ID Tour:").pack(pady=5)
    entry_id_tour = tk.Entry(ventana_reservas)
    entry_id_tour.pack()

    tk.Label(ventana_reservas, text="Fecha Reserva (YYYY-MM-DD):").pack(pady=5)
    entry_fecha = tk.Entry(ventana_reservas)
    entry_fecha.pack()

    tk.Label(ventana_reservas, text="Cantidad de Personas:").pack(pady=5)
    entry_cantidad = tk.Entry(ventana_reservas)
    entry_cantidad.pack()

    tk.Button(ventana_reservas, text="Agregar Reserva", command=agregar).pack(pady=20)

# Ventana principal
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Sistema de Reservas")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Gestión de Reservas", font=("Arial", 16)).pack(pady=10)

    tk.Button(ventana, text="Gestión de Clientes", command=gestion_clientes).pack(pady=10)
    tk.Button(ventana, text="Gestión de Tours", command=gestion_tours).pack(pady=10)
    tk.Button(ventana, text="Gestión de Reservas", command=gestion_reservas).pack(pady=10)

    ventana.mainloop()

ventana_principal()
