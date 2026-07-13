def test_validar_nombre_usuario(usuario):

    assert usuario["nombre"] == "Antonio"

def test_validar_estado_usuario(usuario):

    assert usuario["activo"] == True