
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