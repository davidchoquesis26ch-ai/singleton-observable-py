class SingletonObservable:
    """Base reutilizable: da Singleton + Observer a cualquier clase que herede de ella."""
    _instancias = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instancia = super().__new__(cls)
            instancia._observadores = []
            cls._instancias[cls] = instancia
        return cls._instancias[cls]

    def suscribir(self, funcion_observadora):
        self._observadores.append(funcion_observadora)

    def notificar(self, *args, **kwargs):
        for funcion in self._observadores:
            funcion(*args, **kwargs)
            
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