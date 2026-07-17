# Ejercicio 1

# Importa:

# from unittest.mock import Mock

# Crea un objeto:

# usuario = Mock()

# Asígnale:

# usuario.nombre = "Antonio"

# Imprime:

# usuario.nombre

from unittest.mock import Mock

usuario = Mock()

usuario.nombre = "Antonio"

print(usuario.nombre)

def test_validar_nombre_usuario():

    assert usuario.nombre == "Antonio"

# Ejercicio 2

# Crea un Mock llamado:

# api

# Agrega un método:

# obtener_status()

# que retorne:

# 200

# Utiliza:

# return_value

api = Mock()

def test_validar_status():

    api.obtener_status.return_value = 200

    assert api.obtener_status() == 200

# Ejercicio 3

# Crea un Mock llamado:

# cliente

# Agrega:

# cliente.nombre = "Ana"
# cliente.edad = 25

# Valida ambos atributos usando assert.

cliente = Mock()

cliente.nombre = "Ana"
cliente.edad = 25

def test_validar_cliente():

    assert cliente.nombre == "Ana"
    assert cliente.edad == 25

# Ejercicio 4

# Simula un método:

# login()

# que retorne:

# True

# Verifica el resultado.

auth = Mock()

auth.login.return_value = True

resultado = auth.login()

def test_validar_login():

    assert resultado is True

# Ejercicio 5

# Llama un método:

# guardar()

# y verifica que fue llamado utilizando:

# assert_called_once()

articulo = Mock()

articulo.guardar.return_value = {
    "id": 1,
    "nombre_articulo": "Smartphone"
}

articulo.guardar()

def test_validar_articulos_guardados():

    articulo.guardar.assert_called_once()

# Ejercicio 6

# Llama:

# enviar_email("admin@test.com")

# Verifica:

# assert_called_with("admin@test.com")

enviar_email = Mock()

enviar_email("admin@test.com")

def test_validar_email():

    enviar_email.assert_called_with("admin@test.com")

# Ejercicio 7

# Llama tres veces:

# api.obtener_usuario()

# Verifica:

# call_count == 3

api = Mock()

def test_validar_llamadas_api():

    api.obtener_usuario()
    api.obtener_usuario()
    api.obtener_usuario()

    assert api.obtener_usuario.call_count == 3

# Ejercicio 8

# Utiliza:

# side_effect

# para que un método retorne:

# 200
# 201
# 500

# en llamadas consecutivas.

api = Mock()

api.obtener_status_code.side_effect = [200, 201, 500]

def test_validar_status_code():

    assert api.obtener_status_code() == 200
    assert api.obtener_status_code() == 201
    assert api.obtener_status_code() == 500

# Ejercicio 9

# Utiliza side_effect para lanzar una excepción:

# ValueError("Error simulado")

# Captúrala con try/except.

empleado = Mock()

empleado.obtener_nombre.side_effect = ValueError("Error simulado")

def test_validar_excepcion_empleado():

    try:
        empleado.obtener_nombre()
    except ValueError as e:
        assert str(e) == "Error simulado"

# Ejercicio 10 (Nivel entrevista)

# Sin ejecutar:

# from unittest.mock import Mock

# api = Mock()

# api.login.return_value = True

# resultado = api.login("admin", "1234")

# Responde:

# ¿Qué contiene resultado? Contiene el valor True, porque así fue el Mock configurado
# ¿Se ejecutó un login real? No, debido a que api es un objeto Mock, por lo tanto no existe una configuración real
# ¿Qué ventaja tiene esto en pruebas unitarias? Aislar el código que se está probando, simular escenarios dificiles de 
#   reproducción en ambientes reales
# ¿Qué diferencia existe entre return_value y side_effect? return_value devuelve siempre el mismo valor;
#   side_effect puede devolver distintos valores en llamadas consecutivas, también permite lanzar excepciones
# ¿En qué situaciones usarías un Mock en un framework de QA Automation? Para simular respuestas de api, base de datos,
#   evitar dependencias con servicios terceros, simular errores