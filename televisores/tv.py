from televisores.marca import Marca

class TV:
    _numTV = 0  # Atributo de clase para contar televisores creados

    def __init__(self, marca: Marca, estado: bool):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    # Métodos de clase
    @classmethod
    def getNumTV(cls) -> int:
        return cls._numTV

    @classmethod
    def setNumTV(cls, numTV: int):
        cls._numTV = numTV

    # Métodos para encender y apagar
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self) -> bool:
        return self._estado

    # Métodos para cambiar canal
    def canalUp(self):
        if self._estado and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self._estado and self._canal > 1:
            self._canal -= 1

    def setCanal(self, canal: int):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    def getCanal(self) -> int:
        return self._canal

    # Métodos para cambiar volumen
    def volumenUp(self):
        if self._estado and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self):
        if self._estado and self._volumen > 0:
            self._volumen -= 1

    def setVolumen(self, volumen: int):
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    def getVolumen(self) -> int:
        return self._volumen

    # Métodos para atributos adicionales
    def setPrecio(self, precio: int):
        self._precio = precio

    def getPrecio(self) -> int:
        return self._precio

    def setMarca(self, marca: Marca):
        self._marca = marca

    def getMarca(self) -> Marca:
        return self._marca

    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control
