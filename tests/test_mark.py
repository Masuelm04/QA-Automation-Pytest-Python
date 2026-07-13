import pytest

@pytest.mark.skip(reason="Esta funcionalidad estará en mantenimiento durante el fin de semana")
def test_enviar_formulario_contacto():
    # Simula la acción de que fallará este fin de semana
    assert True

navegador_actual = "firefox"

@pytest.mark.skipif(navegador_actual != "Chromium", reason="Este servicio solo es compatible con el navegador Chromium")
def test_interaccion_exclusiva_chromium():
    # Esta prueba fallará si no es Chromium
    assert navegador_actual == "Chromium"

@pytest.mark.xfail(reason="Vinculado al defecto CTFL-105")
def test_carrito_rechaza_cantidades_negativas():
    # Simulamos el comportamiento del sistema actual que está roto
    cantidad_ingresada = -5
    assert cantidad_ingresada > 0

@pytest.mark.api
def test_endpoint_usuarios_retorna_200():
    assert True

@pytest.mark.ui
def test_renderizado_menu_navegacion():
    assert True