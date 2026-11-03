# CLAUDE.md

Guía para Claude Code en este repositorio.

- **Proyecto:** prototipo de la tesis UPEA de Jorge Luis Dueñas Lopez. Prioriza vulnerabilidades (hallazgos CVE) de las dependencias dentro del pipeline de CI/CD. El modelo prioriza, no decide: la decisión es del equipo.
- **Forma de explicar:** en español simple. Luis está aprendiendo Git, Docker y CI/CD.
- **Plan y órdenes:** el plan está en `C:\TESIS_UPEA\00_guia\PLAN_PROTOTIPO.md`. Cada sesión trabaja con una orden cerrada de `C:\TESIS_UPEA\00_guia` (`ORDEN_CLAUDE_CODE_<fase>.txt`), que termina con un acuse por ítem. Fuera de `04_prototipo` solo se crea lo que la orden nombra; no se edita nada de `00_guia`.
- **Código:** Python real, ejecutable y comentado en español. Para el modelo, solo scikit-learn; ningún LLM dentro del producto.
- **Secretos:** nunca en el código ni en el repositorio. Van en `.env` (fuera de Git) y en GitHub Secrets. gitleaks revisa cada commit.
- **Placeholder:** el placeholder del clasificador se rotula como andamio en el código y en el comentario del PR.
- **Trazabilidad:** la columna CVE y las de trazabilidad se conservan en todo el flujo y nunca entran al modelo.
- **Comentario en el PR:** es informativo. Solo comenta y no bloquea la aceptación del cambio (decisión del 02/11/2026; el modo bloqueante queda como trabajo futuro).
- **Repositorios ajenos:** se escanean solo en GitHub Actions o en un contenedor desechable, nunca en la PC. El `.joblib` solo se carga si es propio y su SHA-256 coincide.
- **Redacción:** el README y la documentación se escriben con palabras propias. Nunca se copian párrafos del documento de la tesis.
- **Dos capas:** las herramientas de seguridad de este repositorio (pre-commit, gitleaks, ruff, pytest, CodeQL, Dependabot, Trivy) cuidan al propio prototipo. El aporte de la tesis es el prototipo dentro del pipeline del equipo de desarrollo.
- **Forma de trabajar:** Modo Plan antes de programar algo nuevo; pruebas antes de dar algo por terminado. Permisos: Manual o "Aceptar ediciones"; nunca Auto ni "Bypass permissions".
