def test_estatus_Ok():

    response = {
        "status_code": 200,
        "success": True
    }

    assert response["status_code"] == 200

def test_success_response():

    response = {
        "status_code": 200,
        "success": True
    }

    assert response["success"] == True  

def test_key_en_diccionario():

    usuario = {
        "nombre": "Antonio",
        "edad": 25
    } 

    assert "nombre" in usuario

def test_campo_edad():

    usuario = {
        "nombre": "Antonio",
        "edad": 25
    } 

    assert usuario["edad"] == 25