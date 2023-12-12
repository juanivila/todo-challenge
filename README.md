# Execute
### Requirements
- Docker

## Run project
### Linux/MacOS
```bash
make run
```

### Or run docker-compose
```bash
docker-compose up --build
```


### Access documentation
http://0.0.0.0:8000/api/schema/swagger-ui/#/



### Notas 
- Las variables de entorno se encuentran en el repositorio para simplificar el proceso
- El proyecto se encuentra en la rama master
- Se crean dos usuarios por defecto, necesarios para obtener el access token
  - user: admin
  - password: admin
  - user: admin2
  - password: admin
- El filtrado aun no esta documentado en Swagger, pero se puede acceder con estos params: /api/todos?completed=true
- Queda pendiente finalizar los test cases.
