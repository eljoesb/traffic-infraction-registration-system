# Traffic Infraction Registration System

Este proyecto es un sistema de registro de infracciones de tránsito desarrollado en Python. El sistema incluye una interfaz administrativa para gestionar registros y una API para que los oficiales de policía carguen infracciones.

## Características

1. **Interfaz Administrativa**

   - Gestión de personas: nombre y correo electrónico.
   - Gestión de vehículos: placa de patente, marca, color (relacionados con una persona).
   - Gestión de oficiales: nombre y número único identificatorio.
   - Gestión de infracciones: registro de infracciones asociadas a vehículos.

2. **API para Oficiales de Policía**
   - Cargar infracciones a un vehículo mediante un método POST.
   - Autenticación mediante tokens de acceso (Bearer Token).
   - Generar informes de infracciones por correo electrónico de la persona.

## Requisitos

- Python 3.10
- Docker
- Docker Compose

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/eljoesb/traffic-infraction-registration-system.git
   cd traffic-infraction-registration-system
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar Localmente con Docker Compose

1. Asegúrate de que Docker y Docker Compose están instalados en tu sistema.

2. Ejecuta el siguiente comando para levantar los servicios:

   ```bash
   docker-compose up --build
   ```

3. La aplicación estará disponible en:
   - API: `http://localhost:5001`
   - Admin: `http://localhost:5002`

### Publicación en Docker Hub

Las imágenes Docker para este proyecto están disponibles en Docker Hub.

- **API:** [codejonville/traffic-infraction-registration-system-api:latest](https://hub.docker.com/repository/docker/codejonville/traffic-infraction-registration-system-api)
- **Admin:** [codejonville/traffic-infraction-registration-system-admin:latest](https://hub.docker.com/repository/docker/codejonville/traffic-infraction-registration-system-admin)

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, crea un issue o un pull request para cualquier mejora o corrección.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Enlaces

- [Repositorio en GitHub](https://github.com/eljoesb/traffic-infraction-registration-system)
- [Docker Hub - API](https://hub.docker.com/repository/docker/codejonville/traffic-infraction-registration-system-api)
- [Docker Hub - Admin](https://hub.docker.com/repository/docker/codejonville/traffic-infraction-registration-system-admin)
