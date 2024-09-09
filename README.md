# Taller de Git y GitHub*


## **Contexto del Proyecto**

El proyecto **Sistema de Gestión de Vehículos** es una aplicación destinada a gestionar y centralizar toda la información relacionada con vehículos de una flota. Incluye la gestión de detalles técnicos, historial de mantenimiento y la administración general de cada vehículo. 

El objetivo principal es proporcionar una herramienta fácil de usar que permita a los usuarios consultar y actualizar información esencial sobre los vehículos, asegurando que el mantenimiento se realice a tiempo y que todos los aspectos técnicos estén debidamente registrados. La plataforma está diseñada para ser flexible, escalable y apta para empresas que administran flotas de cualquier tamaño.

Las principales características incluyen:
- Gestión técnica del vehículo: Registro de datos técnicos como marca, modelo, año, tipo de combustible, etc.
- Historial de mantenimiento: Seguimiento detallado de las reparaciones, revisiones, y cambios de piezas.
- Administración de vehículos: Capacidad de registrar nuevos vehículos y actualizar su estado.

El equipo de desarrollo está trabajando en este proyecto utilizando **Git y GitHub** para el control de versiones, asegurando la colaboración efectiva y el seguimiento de cambios mediante estándares de commits y ramas bien definidos.

---

### 1. Configuración Inicial y Creación de Repositorio

#### **Pasos:**
1. **Configurar Git en el equipo local:**
   - Abre la terminal (o Git Bash en Windows).
   - Configura tu nombre de usuario y correo electrónico con los comandos:
     ```bash
     git config --global user.name "Tu Nombre"
     git config --global user.email "tuemail@ejemplo.com"
     ```
   - Esto asegura que cada commit esté vinculado a tu identidad.


2. **Clonar el repositorio:**
   - Copia el enlace del repositorio generado.
   - Clona el repositorio en tu computadora local con:
     ```bash
     git clone https://github.com/tu_usuario/tu_repositorio.git
     ```
   - Esto descargará el código a tu máquina local.

Este estándar debe respetarse por todos los miembros del equipo. Cualquier modificación debe ser consensuada y reflejada en este documento.

---

## **Estándar de Commits**

El equipo ha adoptado un sistema de commits semánticos para garantizar que todos los cambios estén bien documentados y que el historial del repositorio sea fácil de seguir. Cada commit debe reflejar de manera precisa y concisa los cambios realizados en el código, lo que facilita el trabajo colaborativo y la gestión del proyecto.

### **Estructura de un Mensaje de Commit**

Un mensaje de commit debe seguir la siguiente estructura:

```
<tipo>(<área>): <descripción breve>

<cuerpo opcional>

<referencias opcionales>
```

### **Tipos de Commits**

- **feat**: Commits que introducen una nueva funcionalidad o característica.
  - Ejemplo: `feat(mantenimiento): agregar función para registrar nuevas reparaciones`
  
- **fix**: Commits que corrigen errores.
  - Ejemplo: `fix(vehículo): corregir error al mostrar la información del tipo de combustible`
  
- **refactor**: Cambios que mejoran el código sin cambiar su funcionalidad.
  - Ejemplo: `refactor(clase vehículo): optimizar método de cálculo de kilometraje`
  
- **docs**: Actualizaciones o modificaciones en la documentación.
  - Ejemplo: `docs(README): actualizar descripción del proyecto`
  
- **style**: Cambios de formato que no afectan el código (indentación, espacios en blanco, formato).
  - Ejemplo: `style(mantenimiento): corregir formato de la clase`
  
- **test**: Añadir o modificar pruebas unitarias o de integración.
  - Ejemplo: `test(historial): agregar pruebas unitarias para la clase Mantenimiento`
  
- **chore**: Cambios menores o tareas del mantenimiento del código que no afectan la funcionalidad.
  - Ejemplo: `chore(deps): actualizar dependencias de la librería de validación`
  
- **perf**: Cambios realizados para mejorar el rendimiento.
  - Ejemplo: `perf(vehículo): optimizar carga de historial de mantenimientos`

### **Descripción Breve**

Debe describir de forma clara y concisa lo que se hizo en el commit. El límite recomendado es de 50 caracteres. Utiliza el modo imperativo (como si estuvieras dando una instrucción). Ejemplos:

- Correcto: `feat: agregar validación en el formulario de registro`
- Incorrecto: `feat: agregando validación en el formulario`
