from abc import ABC, abstractmethod


class cambio(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class LightBulb(cambio):
    def encender(self):
        print("LightBulb: turned on...")

    def apagar(self):
        print("LightBulb: turned off...")


class Fan(cambio):
    def encender(self):
        print("Fan: turned on...")

    def apagar(self):
        print("Fan: turned off...")


class cambioElectrico:

    def __init__(self, c: cambio):
        self.client = c
        self.on = False

    def presionar(self):
        if self.on:
            self.client.apagar()
            self.on = False
        else:
            self.client.encender()
            self.on = True


l = LightBulb()
f = Fan()
switch = cambioElectrico(f)
switch.presionar()
switch.presionar()
switch.presionar()
