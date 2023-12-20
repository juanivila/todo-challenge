# Execute

### Requirements

- Docker

## Run project

```bash
make run
```

## Run tests

```bash
make test 
```

## Or run docker-compose

```bash
docker-compose up --build
```

### Access documentation

http://0.0.0.0:8000/api/schema/swagger-ui/#/

### Notas

- Las variables de entorno se encuentran en el repositorio para simplificar el proceso
- Se crean dos usuarios por defecto, necesarios para obtener el access token
    - user: admin
    - password: admin
    - user: admin2
    - password: admin
