
import tkinter as tk
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

    def buscar_vehiculo_por_comparacion(self, año, comparacion):
        if comparacion == 'mayor':
            return [v for v in self.vehiculos if v.get_año() > año]
        elif comparacion == 'menor':
            return [v for v in self.vehiculos if v.get_año() < año]
        else:
            raise ValueError("Comparación no válida. Use 'mayor' o 'menor'.")
     
    def imprimir_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(f"Marca: {vehiculo.get_marca()}, Modelo: {vehiculo.get_modelo()}, Año: {vehiculo.get_año()}, "
                  f"Kilometraje: {vehiculo.get_kilometraje()}, Estado: {vehiculo.get_estado_actual()}, "
                  f"Combustible: {vehiculo.get_tipo_combustible()}, Color: {vehiculo.get_color()}, "
                  f"Potencia: {vehiculo.get_potencia()} CV")

class VehiculoApp:
    def __init__(self, root):
        self.main = Main()

        self.root = root
        self.root.title("Gestión de Vehículos")

        # Labels y Entradas para los datos del vehículo
        self.lbl_marca = tk.Label(root, text="Marca:")
        self.lbl_marca.grid(row=0, column=0)
        self.entry_marca = tk.Entry(root)
        self.entry_marca.grid(row=0, column=1)

        self.lbl_modelo = tk.Label(root, text="Modelo:")
        self.lbl_modelo.grid(row=1, column=0)
        self.entry_modelo = tk.Entry(root)
        self.entry_modelo.grid(row=1, column=1)

        self.lbl_año = tk.Label(root, text="Año:")
        self.lbl_año.grid(row=2, column=0)
        self.entry_año = tk.Entry(root)
        self.entry_año.grid(row=2, column=1)

        self.lbl_kilometraje = tk.Label(root, text="Kilometraje:")
        self.lbl_kilometraje.grid(row=3, column=0)
        self.entry_kilometraje = tk.Entry(root)
        self.entry_kilometraje.grid(row=3, column=1)

        self.lbl_estado = tk.Label(root, text="Estado Actual:")
        self.lbl_estado.grid(row=4, column=0)
        self.entry_estado = tk.Entry(root)
        self.entry_estado.grid(row=4, column=1)

        self.lbl_combustible = tk.Label(root, text="Tipo de Combustible:")
        self.lbl_combustible.grid(row=5, column=0)
        self.entry_combustible = tk.Entry(root)
        self.entry_combustible.grid(row=5, column=1)

        self.lbl_color = tk.Label(root, text="Color:")
        self.lbl_color.grid(row=6, column=0)
        self.entry_color = tk.Entry(root)
        self.entry_color.grid(row=6, column=1)

        self.lbl_potencia = tk.Label(root, text="Potencia (CV):")
        self.lbl_potencia.grid(row=7, column=0)
        self.entry_potencia = tk.Entry(root)
        self.entry_potencia.grid(row=7, column=1)

        # Botón para agregar vehículo
        self.btn_agregar = tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo)
        self.btn_agregar.grid(row=8, column=0, columnspan=2)

        # Botón para buscar vehículos por año
        self.btn_buscar_año = tk.Button(root, text="Buscar por Año", command=self.buscar_por_año)
        self.btn_buscar_año.grid(row=9, column=0, columnspan=2)

        # Botón para mostrar todos los vehículos
        self.btn_mostrar = tk.Button(root, text="Mostrar Todos", command=self.mostrar_todos)
        self.btn_mostrar.grid(row=10, column=0, columnspan=2)

        # Caja de texto para mostrar resultados
        self.txt_resultados = tk.Text(root, width=50, height=10)
        self.txt_resultados.grid(row=11, column=0, columnspan=2)

    def agregar_vehiculo(self):
        try:
            vehiculo = Vehiculo(
                self.entry_marca.get(),
                self.entry_modelo.get(),
                int(self.entry_año.get()),
                int(self.entry_kilometraje.get()),
                self.entry_estado.get(),
                self.entry_combustible.get(),
                self.entry_color.get(),
                int(self.entry_potencia.get())
            )
            self.main.agregar_vehiculo(vehiculo)
            messagebox.showinfo("Éxito", "Vehículo agregado exitosamente.")
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def buscar_por_año(self):
        try:
            año = int(self.entry_año.get())
            vehiculos = self.main.buscar_vehiculo_por_año(año)
            if vehiculos:
                self.txt_resultados.delete(1.0, tk.END)
                self.txt_resultados.insert(tk.END, "\n".join([v.get_info() for v in vehiculos]))
            else:
                messagebox.showinfo("Resultado", "No se encontraron vehículos para ese año.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un año válido.")

    def mostrar_todos(self):
        self.txt_resultados.delete(1.0, tk.END)
        self.txt_resultados.insert(tk.END, self.main.imprimir_vehiculos())


# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = VehiculoApp(root)
    root.mainloop()