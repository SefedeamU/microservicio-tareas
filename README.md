# Microservicio de Tareas

Este proyecto es un microservicio para la gestión de tareas utilizando FastAPI y PostgreSQL.

## Estructura del Proyecto

- `app/`
  - `api/`
    - `tasks.py`: Endpoints para gestionar tareas.
    - `comments.py`: Endpoints para gestionar comentarios.
  - `core/`
    - `config.py`: Configuraciones generales (BD, CORS, etc.).
  - `crud/`
    - `tasks.py`: Operaciones CRUD para tareas.
    - `comments.py`: Operaciones CRUD para comentarios.
  - `db/`
    - `base.py`: Base declarativa para SQLAlchemy.
    - `models.py`: Definición de los modelos Tareas y Comentarios.
    - `session.py`: Manejo de la sesión de SQLAlchemy.
  - `schemas/`
    - `task.py`: Esquemas Pydantic para validación de Tareas.
    - `comment.py`: Esquemas Pydantic para validación de Comentarios.
  - `main.py`: Punto de entrada para FastAPI.
  - `initial_data.py`: Script opcional para agregar datos iniciales (opcional).

## Configuración

1. Clonar el repositorio.
2. Crear un archivo `.env` con la URL de la base de datos.
3. Construir y ejecutar los contenedores Docker:
   ```sh
   docker-compose up --build