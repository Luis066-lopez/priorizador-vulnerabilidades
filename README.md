# priorizador-vulnerabilidades

Prototipo de una tesis de grado de Ingeniería de Sistemas de la Universidad Pública de El Alto (UPEA).

La idea es sencilla: cuando un equipo sube cambios a su repositorio, su pipeline de CI/CD revisa las librerías de las que depende el proyecto, encuentra las que tienen vulnerabilidades conocidas (identificadas con un CVE) y este sistema las ordena según cuáles conviene atender primero. Para ordenarlas usa un modelo de aprendizaje supervisado entrenado con scikit-learn.

El resultado llega como un comentario en el Pull Request. Ese comentario solo informa: no bloquea el cambio. La decisión de qué corregir y cuándo siempre es del equipo.

## Estado

**Fase F0: preparación.** Por ahora el repositorio tiene la estructura básica, una prueba de humo y los controles de seguridad del propio proyecto. El código de la aplicación (API, enriquecimiento de datos, modelo y tablero) llega en las fases siguientes.

## Qué hay aquí

| Carpeta o archivo | Para qué sirve |
|---|---|
| `src/priorizador/` | El paquete de Python del sistema (por ahora solo su versión). |
| `tests/` | Pruebas automáticas con pytest. |
| `docs/` | Documentación del proyecto (los requerimientos están pendientes). |
| `.github/` | La CI en GitHub Actions y la configuración de Dependabot. |
| `.env.example` | Los nombres de las variables de entorno que el sistema necesitará, sin valores. |

## Cómo correr las pruebas en Windows

Hace falta Python 3.12.

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
pre-commit install
pytest
```

## Seguridad del propio repositorio

- Antes de cada commit, **pre-commit** corre **gitleaks** (frena cualquier clave o token que se quiera subir por error) y **ruff** (revisa el estilo y patrones inseguros del código).
- En cada push y en cada Pull Request, la **CI** vuelve a correr ruff, las pruebas y **pip-audit** (busca vulnerabilidades en las dependencias de desarrollo).
- En GitHub están activos **CodeQL** (análisis del código y de los workflows) y las alertas de **Dependabot**.
- Los secretos nunca se guardan en el repositorio: van en un archivo `.env` local, que Git ignora, o en GitHub Secrets.

## Convenciones

El código y sus comentarios se escriben en español.

## Licencia

MIT. Ver [LICENSE](LICENSE).
