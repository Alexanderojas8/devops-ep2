# Política de seguridad

## Cómo reportar una vulnerabilidad

Si encuentras un problema de seguridad en este repositorio, no lo publiques en un issue abierto. Usa la pestaña **Security** del repositorio en GitHub (Report a vulnerability) o contacta directamente a los integrantes, Alexander Rojas y Niover Guevara, a través de GitHub.

Incluye en el reporte: qué componente afecta, cómo reproducirlo y qué impacto crees que tiene.

## Versiones con soporte

| Versión | Soporte |
|---|---|
| Última versión en `main` | Sí |
| Versiones anteriores | No |

## Medidas de seguridad del proyecto

- **Análisis de dependencias con Snyk** en cada push y Pull Request. El pipeline falla ante vulnerabilidades de severidad alta o crítica, y en ese caso no se publican imágenes ni se despliega.
- **Dependabot** revisa semanalmente Maven, pip, los Dockerfile y las acciones de GitHub, y abre solicitudes de actualización. Las alertas y las actualizaciones de seguridad están activas.
- **Push protection** de GitHub bloquea los pushes que contienen secretos detectables.
- **Secretos** guardados como secretos del repositorio (`SNYK_TOKEN`) y nunca dentro del código.
- **Contenedores** con límite de memoria y CPU y con la opción `no-new-privileges`, definidos en `docker-compose.deploy.yml`.
- **Imágenes trazables**, etiquetadas con el hash del commit que las generó.

## Qué esperar tras un reporte

Se revisará el reporte, se confirmará si afecta al proyecto y, de ser así, se corregirá actualizando la dependencia o el código afectado. El cambio pasará por el pipeline antes de publicarse.
