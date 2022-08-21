import string
import random

class infoVehiculo:
    
    def __init__(self, marca, electrico, catalogo_precios):
        self.marca = marca
        self.electrico = electrico
        self.catalogo_precios = catalogo_precios

    def compute_tax(self):
        tax_porcentaje = 0.05
        if self.electrico:
            tax_porcentaje = 0.02
        return tax_porcentaje * self.catalogo_precios

    def print(self):
        print(f"marca: {self.marca}")
        print(f"Payable tax: {self.compute_tax()}")

class vehiculo:

    def __init__(self, id, placa, info):
        self.id = id
        self.placa = placa
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License plate: {self.placa}")
        self.info.print()


class registroVehiculos:

    def __init__(self):
        self.vehiculo_info = { }
        self.add_vehiculo_info("Tesla Model 3", True, 60000)
        self.add_vehiculo_info("Volkswagen ID3", True, 35000)
        self.add_vehiculo_info("BMW 5", False, 45000)
        self.add_vehiculo_info("Tesla Model Y", True, 75000)

    def add_vehiculo_info(self, marca, electrico, catalogo_precios):
        self.vehiculo_info[marca] = infoVehiculo(marca, electrico, catalogo_precios)

    def generar_vehiculo_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generar_vehiculo_licensia(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehiculo(self, marca):
        id = self.generar_vehiculo_id(12)
        placa = self.generar_vehiculo_licensia(id)
        return vehiculo(id, placa, self.vehiculo_info[marca])


class Application:

    def registro_vehiculo(self, marca: string):
        # create a registro instance
        registro = registroVehiculos()

        vehiculo = registro.create_vehiculo(marca)

        # print out the vehiculo information
        vehiculo.print()

app = Application()
app.registro_vehiculo("Volkswagen ID3")
app.registro_vehiculo("Tesla Model Y")

