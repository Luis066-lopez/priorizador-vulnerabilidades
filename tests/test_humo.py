"""Prueba de humo: el paquete se importa y tiene la version esperada."""

import priorizador


def test_version_del_paquete():
    # Si falla, el paquete no se pudo importar o la version no coincide con la de F0.
    assert priorizador.__version__ == "0.1.0"
