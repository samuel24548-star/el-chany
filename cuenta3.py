import tkinter as tk
from datetime import datetime

saldo = 1000  # Saldo inicial
movimientos = []  # Lista para almacenar los movimientos

# Diccionario con los datos del cliente
cliente = {"nombre": "", "apellido": "", "domicilio": "", "fecha_nac": ""}

# Función para agregar un cargo (gasto)
def agregar_cargo():
    global saldo
    if not guardar_cliente():  # Verifica si los datos del cliente son válidos
        return
    try:
        monto = float(entrada_monto.get())  # Convierte el monto a número
    except:
        etiqueta.config(text="Monto inválido")  # Muestra error si el monto no es válido
        return
    if monto > saldo:  # Verifica si hay suficiente saldo
        etiqueta.config(text="Saldo insuficiente")
        return
    saldo -= monto  # Resta el monto al saldo
    # Agrega el movimiento con tipo, descripción, monto, saldo y fecha
    movimientos.append({"tipo": "CARGO", "desc": entrada_desc.get(), "monto": monto, "saldo": saldo, "fecha": datetime.now()})
    etiqueta.config(text=f"Saldo actual: {saldo:.2f}")
    limpiar_campos()
    mostrar_ticket()

# Función para agregar un abono (depósito)
def agregar_abono():
    global saldo
    if not guardar_cliente():  # Verifica si los datos del cliente son válidos
        return
    try:
        monto = float(entrada_monto.get())  # Convierte el monto a número
    except:
        etiqueta.config(text="Monto inválido")  # Muestra error si el monto no es válido
        return
    saldo += monto  # Suma el monto al saldo
    # Agrega el movimiento con tipo, descripción, monto, saldo y fecha
    movimientos.append({"tipo": "ABONO", "desc": entrada_desc.get(), "monto": monto, "saldo": saldo, "fecha": datetime.now()})
    etiqueta.config(text=f"Saldo actual: {saldo:.2f}")
    limpiar_campos()
    mostrar_ticket()

# Función para guardar los datos del cliente
def guardar_cliente():
    nombre = entrada_nombre.get().strip()
    apellido = entrada_apellido.get().strip()
    if not nombre or not apellido:  # Verifica si nombre y apellido están completos
        etiqueta.config(text="Por favor, ingrese nombre y apellido")
        return False
    # Guarda la información del cliente
    cliente["nombre"] = nombre
    cliente["apellido"] = apellido
    cliente["domicilio"] = entrada_domicilio.get().strip()
    cliente["fecha_nac"] = entrada_fecha_nac.get().strip()
    return True

# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_desc.delete(0, tk.END)
    entrada_monto.delete(0, tk.END)

# Función para mostrar el ticket con el historial de movimientos
def mostrar_ticket():
    texto.delete(1.0, tk.END)  # Limpia el área de texto
    texto.insert(tk.END, "===== TICKET ESTADO DE CUENTA =====\n")
    texto.insert(tk.END, f"Cliente: {cliente['nombre']} {cliente['apellido']}\n")
    texto.insert(tk.END, f"Domicilio: {cliente['domicilio']}\n")
    texto.insert(tk.END, f"Fecha Nac.: {cliente['fecha_nac']}\n")
    texto.insert(tk.END, f"Saldo inicial: $1000.00\n")
    texto.insert(tk.END, "-"*50 + "\n")
    for m in movimientos:
        # Formatea la fecha y muestra cada movimiento
        fecha_str = m["fecha"].strftime("%Y-%m-%d %H:%M")
        texto.insert(tk.END, f"{fecha_str:<20}{m['tipo']:<8}{m['desc']:<15}{m['monto']:>8.2f}{m['saldo']:>10.2f}\n")
    texto.insert(tk.END, "-"*50 + "\n")
    texto.insert(tk.END, f"Saldo final: {saldo:.2f}\n")
    texto.insert(tk.END, "Gracias por su preferencia\n")
    texto.insert(tk.END, "="*50 + "\n")

# Creación de la ventana y los componentes de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Estado de Cuenta Simple - Ticket")

# Campos de entrada para los datos del cliente
tk.Label(ventana, text="Nombre Cliente").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Apellido Cliente").pack()
entrada_apellido = tk.Entry(ventana)
entrada_apellido.pack()

tk.Label(ventana, text="Domicilio").pack()
entrada_domicilio = tk.Entry(ventana)
entrada_domicilio.pack()

tk.Label(ventana, text="Fecha de Nacimiento (YYYY-MM-DD)").pack()
entrada_fecha_nac = tk.Entry(ventana)
entrada_fecha_nac.pack()

# Campos para el movimiento de cuenta (Descripción y Monto)
tk.Label(ventana, text="Descripción Movimiento").pack()
entrada_desc = tk.Entry(ventana)
entrada_desc.pack()

tk.Label(ventana, text="Monto").pack()
entrada_monto = tk.Entry(ventana)
entrada_monto.pack()

# Botones para agregar cargos y abonos
btn_cargo = tk.Button(ventana, text="Agregar Cargo", command=agregar_cargo)
btn_cargo.pack(pady=5)

btn_abono = tk.Button(ventana, text="Agregar Monto", command=agregar_abono)
btn_abono.pack(pady=5)

# Etiqueta para mostrar el saldo actual
etiqueta = tk.Label(ventana, text=f"Saldo inicial: {saldo}")
etiqueta.pack()

# Área de texto para mostrar el ticket
texto = tk.Text(ventana, height=20, width=60)
texto.pack()

ventana.mainloop()  # Inicia la interfaz gráfica
