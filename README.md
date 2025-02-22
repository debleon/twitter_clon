# Twitter Clone API
Este proyecto es un clon de Twitter desarrollado con FastAPI y PostgreSQL, desplegado en contenedores Docker.

## 🚀 Requisitos
- Docker y Docker Compose instalados en el sistema.

## 🔧 Instalación y ejecución
###  Clonar el repositorio
```bash
git clone https://github.com/debleon/twitter_clon.git
cd twitter_clon
```

### 3 Construir y ejecutar los contenedores
Ejecuta el siguiente comando:
```bash
docker-compose up --build
```
Esto iniciará la base de datos PostgreSQL y la API en FastAPI.

### 4Acceder a la API
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

