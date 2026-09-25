import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from singleton_observable import SingletonObservable

# --- Gestores de Datos ---
class GestorPrestamos(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "prestamos"):
            self.prestamos = []
    def registrar(self, prestamo):
        self.prestamos.append(prestamo)
        self.notificar(prestamo)

class GestorVentas(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "ventas"):
            self.ventas = []
    def registrar(self, venta):
        self.ventas.append(venta)
        self.notificar(venta)

class GestorAerolinea(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "vuelos"):
            self.vuelos = []
    def registrar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
        self.notificar(vuelo)

class GestorJoyeria(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "joyas"):
            self.joyas = []
    def registrar_joya(self, joya):
        self.joyas.append(joya)
        self.notificar(joya)

# --- Ventana Principal ---
app = ttk.Window(title="Demo - Librería SingletonObservable (D.A.C.E.)", themename="flatly")
app.geometry("720x480")

notebook = ttk.Notebook(app)
notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

# ==========================================
# Pestaña 1: Biblioteca (D.A.C.E.)
# ==========================================
tab_biblioteca = ttk.Frame(notebook)
notebook.add(tab_biblioteca, text="Biblioteca (D.A.C.E.)")

tabla_prestamos = ttk.Treeview(tab_biblioteca, columns=("libro", "multa"), show="headings")
tabla_prestamos.heading("libro", text="Libro")
tabla_prestamos.heading("multa", text="Multa ($)")
tabla_prestamos.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_biblioteca = GestorPrestamos()

def refrescar_prestamos(_=None):
    tabla_prestamos.delete(*tabla_prestamos.get_children())
    for p in gestor_biblioteca.prestamos:
        tabla_prestamos.insert("", "end", values=(p["libro"], p["multa"]))

gestor_biblioteca.suscribir(refrescar_prestamos)

ttk.Button(
    tab_biblioteca, 
    text="Agregar préstamo de prueba", 
    bootstyle="success",
    command=lambda: gestor_biblioteca.registrar({"libro": "1984", "multa": 5.0})
).pack(pady=8)

# ==========================================
# Pestaña 2: Juguetería (D.A.C.E.)
# ==========================================
tab_jugueteria = ttk.Frame(notebook)
notebook.add(tab_jugueteria, text="Juguetería (D.A.C.E.)")

tabla_ventas = ttk.Treeview(tab_jugueteria, columns=("juguete", "total"), show="headings")
tabla_ventas.heading("juguete", text="Juguete")
tabla_ventas.heading("total", text="Total ($)")
tabla_ventas.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_jugueteria = GestorVentas()

def refrescar_ventas(_=None):
    tabla_ventas.delete(*tabla_ventas.get_children())
    for v in gestor_jugueteria.ventas:
        tabla_ventas.insert("", "end", values=(v["juguete"], v["total"]))

gestor_jugueteria.suscribir(refrescar_ventas)

ttk.Button(
    tab_jugueteria, 
    text="Agregar venta de prueba", 
    bootstyle="success",
    command=lambda: gestor_jugueteria.registrar({"juguete": "Robot", "total": 150.0})
).pack(pady=8)

# ==========================================
# Pestaña 3: Aerolínea (D.A.C.E.)
# ==========================================
tab_aerolinea = ttk.Frame(notebook)
notebook.add(tab_aerolinea, text="Aerolínea (D.A.C.E.)")

tabla_vuelos = ttk.Treeview(tab_aerolinea, columns=("destino", "precio"), show="headings")
tabla_vuelos.heading("destino", text="Destino")
tabla_vuelos.heading("precio", text="Precio ($)")
tabla_vuelos.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_aerolinea = GestorAerolinea()

def refrescar_vuelos(_=None):
    tabla_vuelos.delete(*tabla_vuelos.get_children())
    for vuelo in gestor_aerolinea.vuelos:
        tabla_vuelos.insert("", "end", values=(vuelo["destino"], vuelo["precio"]))

gestor_aerolinea.suscribir(refrescar_vuelos)

ttk.Button(
    tab_aerolinea, 
    text="Agregar vuelo de prueba", 
    bootstyle="info",
    command=lambda: gestor_aerolinea.registrar_vuelo({"destino": "Cochabamba", "precio": 350.0})
).pack(pady=8)

# ==========================================
# Pestaña 4: Joyería (D.A.C.E.)
# ==========================================
tab_joyeria = ttk.Frame(notebook)
notebook.add(tab_joyeria, text="Joyería (D.A.C.E.)")

tabla_joyas = ttk.Treeview(tab_joyeria, columns=("articulo", "quilates"), show="headings")
tabla_joyas.heading("articulo", text="Artículo")
tabla_joyas.heading("quilates", text="Quilates")
tabla_joyas.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_joyeria = GestorJoyeria()

def refrescar_joyas(_=None):
    tabla_joyas.delete(*tabla_joyas.get_children())
    for joya in gestor_joyeria.joyas:
        tabla_joyas.insert("", "end", values=(joya["articulo"], joya["quilates"]))

gestor_joyeria.suscribir(refrescar_joyas)

ttk.Button(
    tab_joyeria, 
    text="Agregar joya de prueba", 
    bootstyle="warning",
    command=lambda: gestor_joyeria.registrar_joya({"articulo": "Anillo de Oro", "quilates": "18k"})
).pack(pady=8)

if __name__ == "__main__":
    app.mainloop()