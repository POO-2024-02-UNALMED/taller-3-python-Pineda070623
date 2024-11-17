from televisores.tv import TV

class Control:
    def __init__(self):
        self._tv = None  # Atributo protegido

    def enlazar(self, tv: TV):
        self._tv = tv
        tv.setControl(self)

    # Métodos para manejar el televisor
    def turnOn(self):
        if self._tv:
            self._tv.turnOn()

    def turnOff(self):
        if self._tv:
            self._tv.turnOff()

    def canalUp(self):
        if self._tv:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv:
            self._tv.canalDown()

    def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()

    def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()

    def setCanal(self, canal: int):
        if self._tv:
            self._tv.setCanal(canal)

    def setVolumen(self, volumen: int):
        if self._tv:
            self._tv.setVolumen(volumen)

    def getTv(self) -> TV:
        return self._tv

    def setTv(self, tv: TV):
        self._tv = tv
