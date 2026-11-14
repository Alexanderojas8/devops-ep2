# Guía de contribución

Gracias por aportar a `devops-ep2`. Este documento explica cómo trabajar en el repositorio para que el pipeline siga pasando y los cambios sean trazables.

## Flujo de trabajo

1. Crear una rama desde `main` con un nombre descriptivo, por ejemplo `feature/nuevo-endpoint` o `fix/version-dependencia`.
2. Hacer cambios pequeños y commits frecuentes.
3. Probar en local antes de subir (ver más abajo).
4. Subir la rama y abrir un Pull Request hacia `main`.
5. Esperar a que el pipeline termine en verde. Si falla, corregir en la misma rama.
6. Fusionar el Pull Request solo cuando todos los jobs hayan pasado.

## Mensajes de commit

Escribir el mensaje en español, en una línea, con un verbo en presente que diga qué cambia:

- `Agrega endpoint de multiplicar en servicio-python`
- `Corrige version de jackson en el pom.xml`
- `Actualiza documentacion del pipeline`

Evitar mensajes como `cambios` o `arreglos`, porque no permiten rastrear qué pasó.

## Pruebas en local

**Java** (desde `servicio-java`):

```bash
.\mvnw.cmd test
```

**Python** (desde `servicio-python`, con el entorno virtual activo):

```bash
pytest
```

**Todo junto con Docker** (desde la raíz, con Docker Desktop abierto):

```bash
docker compose up --build
```

## Qué revisa el pipeline

Cada push y cada Pull Request ejecutan: pruebas de Java y Python, análisis de seguridad con Snyk, construcción de imágenes Docker y, en `main`, un despliegue simulado. Un cambio que rompa una prueba o introduzca una vulnerabilidad de severidad alta o crítica queda bloqueado y no se publica.

## Dependencias

- No fijar versiones al azar: si Snyk reporta una vulnerabilidad, subir la dependencia a la versión que indica el reporte.
- Las solicitudes de Dependabot se revisan de a una. Se aceptan solo si el pipeline pasa en verde. Los saltos de versión mayor se prueban primero en local.

## Secretos

Nunca subir tokens, contraseñas ni claves al repositorio. El token de Snyk vive como secreto del repositorio (`SNYK_TOKEN`). GitHub bloquea los pushes que contienen secretos detectables.

## Estructura de carpetas

- `servicio-java/`: microservicio Java (código, pruebas y Dockerfile).
- `servicio-python/`: microservicio Python (código, pruebas y Dockerfile).
- `.github/workflows/ci.yml`: definición del pipeline.
- `docs/evidencias/`: capturas del pipeline para la documentación.
