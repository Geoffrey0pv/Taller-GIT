
class Vehiculo:
    VALID_FUEL_TYPES = ['Gasolina', 'Diesel', 'Eléctrico']

    def _init_(self, marca, modelo, año, kilometraje, estado_actual, tipo_combustible, potencia):
        if tipo_combustible not in Vehiculo.VALID_FUEL_TYPES:
            raise ValueError(f"Tipo de combustible no válido. Debe ser uno de {Vehiculo.VALID_FUEL_TYPES}")
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._kilometraje = kilometraje
        self._estado_actual = estado_actual
        self._tipo_combustible = tipo_combustible
        self._potencia = potencia

    # Getter and Setter for potencia
    def get_potencia(self):
        return self._potencia

    def set_potencia(self, potencia):
        self._potencia = potencia

class HistorialMantenimiento:
    def _init_(self, fecha, descripcion_servicio, kilometraje_en_servicio, costo, nombre_mecanico):
        self._fecha = fecha
        self._descripcion_servicio = descripcion_servicio
        self._kilometraje_en_servicio = kilometraje_en_servicio
        self._costo = costo
        self._nombre_mecanico = nombre_mecanico

    # Getters
    def get_fecha(self):
        return self._fecha

    def get_descripcion_servicio(self):
        return self._descripcion_servicio

    def get_kilometraje_en_servicio(self):
        return self._kilometraje_en_servicio

    def get_costo(self):
        return self._costo

    def get_nombre_mecanico(self):
        return self._nombre_mecanico

    # Setters
    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_descripcion_servicio(self, descripcion_servicio):
        self._descripcion_servicio = descripcion_servicio

    def set_kilometraje_en_servicio(self, kilometraje_en_servicio):
        self._kilometraje_en_servicio = kilometraje_en_servicio

    def set_costo(self, costo):
        self._costo = costo

    def set_nombre_mecanico(self, nombre_mecanico):
        self._nombre_mecanico = nombre_mecanico

class Main:
    def _init_(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def buscar_vehiculo_por_año(self, año):
        return [v for v in self.vehiculos if v.get_año() == año]
      
    def imprimir_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(f"Marca: {vehiculo.get_marca()}, Modelo: {vehiculo.get_modelo()}, Año: {vehiculo.get_año()}, "
                  f"Kilometraje: {vehiculo.get_kilometraje()}, Estado: {vehiculo.get_estado_actual()}, "
                  f"Combustible: {vehiculo.get_tipo_combustible()}")

