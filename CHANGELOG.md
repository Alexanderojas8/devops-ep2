# Registro de cambios

Todos los cambios relevantes de este proyecto se documentan aquí.

## [1.0.0] - 2026-11

### Agregado

- Microservicio Java (Spring Boot, Maven) con endpoints `/saludo` y `/sumar`, y sus pruebas unitarias con JaCoCo.
- Microservicio Python (FastAPI) con endpoints `/saludo` y `/restar`, y sus pruebas con PyTest.
- Un Dockerfile por servicio. El de Java usa dos etapas para dejar una imagen liviana.
- `docker-compose.yml` para desarrollo, que construye ambos servicios.
- Pipeline en GitHub Actions con pruebas de Java y Python en cada push y Pull Request.
- Análisis de seguridad con Snyk, que bloquea el pipeline ante vulnerabilidades de severidad alta o crítica.
- Construcción y publicación de las imágenes en GitHub Container Registry, etiquetadas con el hash del commit.
- Dependabot para Maven, pip, Docker y GitHub Actions.
- `docker-compose.deploy.yml` y job de despliegue simulado, con verificación de que ambos servicios responden y con límites de memoria y CPU.
- Documentación: README, evidencias del pipeline, guía de contribución y política de seguridad.

### Corregido

- Permiso de ejecución de `mvnw` en el job de Snyk, que impedía el escaneo del servicio Java.
- Spring Boot actualizado de 4.0.0 a 4.0.9 para resolver 49 de las 50 vulnerabilidades detectadas por Snyk.
- `jackson-databind` fijado en 3.1.8 para resolver la vulnerabilidad crítica restante.
- `fastapi` actualizado a 0.162.2 para resolver las 5 vulnerabilidades de `starlette`.
