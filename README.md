# Microservicio de Tareas

Este proyecto es un microservicio para la gestión de tareas utilizando **FastAPI** y **PostgreSQL**.

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
  - `schemas`/
    - `task.py`: Esquemas Pydantic para validación de Tareas.
    - `comment.py`: Esquemas Pydantic para validación de Comentarios.
  - `main.py`: Punto de entrada para FastAPI.
  - `initial_data.py`: Script opcional para agregar datos iniciales (opcional).


## Configuración

1. Clonar el repositorio.
2. Crear un archivo `.env` con la URL de la base de datos.
3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación:

   ```bash
   uvicorn app.main:app --reload
   ```

## Uso

**Tareas:**  
- **GET /tasks/**: Obtener todas las tareas.
- **POST /tasks/**: Crear una nueva tarea.
- **GET /tasks/{task_id}**: Obtener una tarea por ID.
- **PUT /tasks/{task_id}**: Actualizar una tarea por ID.
- **DELETE /tasks/{task_id}**: Eliminar una tarea por ID.

**Comentarios:**
- **GET /comments/**: Obtener todos los comentarios.
- **POST /comments/**: Crear un nuevo comentario.
- **GET /comments/{comment_id}**: Obtener un comentario por ID.
- **PUT /comments/{comment_id}**: Actualizar un comentario por ID.
- **DELETE /comments/{comment_id}**: Eliminar un comentario por ID.

## Endpoints

### Tareas:
- **GET /tasks/**: Obtener todas las tareas.
- **POST /tasks/**: Crear una nueva tarea.
    - **Body**:
      ```json
      {
        "nombre": "string",
        "descripcion": "string",
        "estado": "string",
        "proyecto_id": 0,
        "responsable_id": 0,
        "fecha_vencimiento": "string"
      }
      ```
- **GET /tasks/{task_id}**: Obtener una tarea por ID.
- **PUT /tasks/{task_id}**: Actualizar una tarea por ID.
    - **Body**:
      ```json
      {
        "nombre": "string",
        "descripcion": "string",
        "estado": "string",
        "proyecto_id": 0,
        "responsable_id": 0,
        "fecha_vencimiento": "string"
      }
      ```
- **DELETE /tasks/{task_id}**: Eliminar una tarea por ID.

### Comentarios:
- **GET /comments/**: Obtener todos los comentarios.
- **POST /comments/**: Crear un nuevo comentario.
    - **Body**:
      ```json
      {
        "tarea_id": 0,
        "contenido": "string",
        "usuario_id": 0
      }
      ```
- **GET /comments/{comment_id}**: Obtener un comentario por ID.
- **PUT /comments/{comment_id}**: Actualizar un comentario por ID.
    - **Body**:
      ```json
      {
        "tarea_id": 0,
        "contenido": "string",
        "usuario_id": 0
      }
      ```
- **DELETE /comments/{comment_id}**: Eliminar un comentario por ID.
- 
### Ejemplo de `.env` para las variables de entorno de la base de datos:

```ini
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_base_datos
```

## Contribuir

1. Hacer un fork del repositorio.
2. Crear una nueva rama:

   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. Realizar los cambios necesarios y hacer commit:

   ```bash
   git commit -am 'Añadir nueva funcionalidad'
   ```

4. Hacer push a la rama:

   ```bash
   git push origin feature/nueva-funcionalidad
   ```

5. Crear un Pull Request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia **MIT**.
