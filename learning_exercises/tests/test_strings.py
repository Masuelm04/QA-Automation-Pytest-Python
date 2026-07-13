def test_nombre_usuario():

    nombre = "Antonio"

    assert nombre == "Antonio"

def test_usuario_activo():

    activo = True

    assert activo == True

def test_edad_entre_18_y_30():

    edad = 22

    assert 18 <= edad < 30

def test_longitud_lista_usuarios():

    usuarios = [
        "Ana",
        "Pedro",
        "Juan"
    ]

    assert len(usuarios) == 3

def test_usuario_existe():

    usuarios = [
        "Ana",
        "Pedro",
        "Juan"
    ]

    assert "Juan" in usuarios
