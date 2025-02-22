# Twitter Clone API
Este proyecto es un clon de Twitter desarrollado con FastAPI y PostgreSQL, desplegado en contenedores Docker.

## 🚀 Requisitos
- Docker y Docker Compose instalados en el sistema.

## 🔧 Instalación y ejecución
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/twitter_clone.git
cd twitter_clone
```

### 2️⃣ Configurar variables de entorno
Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```env
DATABASE_URL=postgresql://user:password@db/twitter_clone
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3️⃣ Construir y ejecutar los contenedores
Ejecuta el siguiente comando:
```bash
docker-compose up --build
```
Esto iniciará la base de datos PostgreSQL y la API en FastAPI.

### 4️⃣ Acceder a la API
Una vez ejecutado el proyecto, puedes acceder a la documentación interactiva de la API en:
- 📌 **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 📌 **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🛑 Detener los contenedores
Para detener los contenedores, usa:
```bash
docker-compose down
```

## 🛠️ Migraciones y base de datos
Si necesitas realizar migraciones manuales con SQLAlchemy, ejecuta:
```bash
docker-compose exec api alembic upgrade head
```

## 📜 Licencia
Este proyecto está bajo la licencia MIT.
