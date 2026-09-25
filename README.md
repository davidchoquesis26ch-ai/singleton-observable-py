# singleton-observable-py

Una clase base reutilizable que agrega los patrones Singleton y Observer
a cualquier clase de Python, sin tener que reescribir el mecanismo cada vez.

## Instalación

Copia `singleton_observable.py` a tu proyecto (por ahora no está publicada en PyPI).

## Uso básico

```python
from singleton_observable import SingletonObservable

class MiGestor(SingletonObservable):
    def __init__(self):
        if not hasattr(self, "datos"):
            self.datos = []

    def registrar(self, dato):
        self.datos.append(dato)
        self.notificar(dato)
,,,

## Por qué usarla

- Garantiza una única instancia por cada clase que herede de ella (Singleton).
- Permite suscribir funciones que se ejecutan automáticamente ante cada evento (Observer).
- Cada clase que hereda mantiene su propio singleton, sin mezclarse con otras.

## Licencia

MIT - ver el archivo LICENSE.