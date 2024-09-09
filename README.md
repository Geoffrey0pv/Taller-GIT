# Taller de Git y GitHub*

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

---

## **Estandar de Commits**
- Todos los commits deben seguir la convención de mensajes:
  - **feat**: Para agregar una nueva funcionalidad.
  - **fix**: Para corregir errores.
  - **docs**: Para actualizar la documentación.
  - **style**: Para cambios que no afectan la lógica del código (formato, espacios, etc.).

**Ejemplo**:
```bash
git commit -m "feat: agregar validación al formulario de registro de vehículos"
```

---

Este estándar debe respetarse por todos los miembros del equipo. Cualquier modificación debe ser consensuada y reflejada en este documento.

---

Este formato proporcionará consistencia a lo largo del proyecto y asegurará que el código sea legible y mantenible por todos los miembros del equipo.

#### **Preguntas:**

- **¿Cuál es la diferencia entre clonar un repositorio y hacer un fork?**
  - **Clonar:** Descargar una copia exacta del repositorio a tu máquina local para trabajar en ella. Las modificaciones que hagas en tu copia local se pueden subir directamente al repositorio remoto, si tienes permisos.
  - **Fork:** Crear una copia del repositorio en tu cuenta de GitHub. Usas un fork cuando no tienes permisos directos para modificar el repositorio original. Las contribuciones se envían mediante pull requests.

- **¿Cuándo usar cada uno?**
  - **Clonar** lo usarías si tienes acceso directo al repositorio y trabajas en colaboración con un equipo que ya tiene permisos.
  - **Fork** es útil cuando quieres contribuir a un proyecto del que no eres miembro, como proyectos de código abierto o repositorios públicos.
