# QA Automation with Pytest

> Repositorio de aprendizaje práctico de **Pytest** orientado a **QA Automation** utilizando **Python**.
>
> Aquí documento mi progreso mediante ejercicios, ejemplos y desafíos que cubren desde los fundamentos hasta conceptos más avanzados de Pytest.

---

# 📚 Objetivos

Este repositorio tiene como propósito practicar y comprender los conceptos más importantes de **Pytest** mediante ejercicios progresivos.

Entre los temas trabajados se encuentran:

- Assertions
- Fixtures
- Fixture Scope
- Chained Fixtures
- Parametrización
- Marks
- Mock
- Patch
- Colecciones
- Organización de pruebas
- Buenas prácticas
- Ejercicios tipo entrevista para QA Automation

---

# 🛠️ Tecnologías

- Python 3.x
- Pytest
- unittest.mock

---

# 📁 Estructura del proyecto

```text
QA-AUTOMATION-PYTEST/
│
├── learning_exercises/
│   ├── tests/
│   │   ├── test_math.py
│   │   ├── test_strings.py
│   │   ├── test_number.py
│   │   ├── test_usuario.py
│   │   ├── test_collections.py
│   │   ├── test_mark.py
│   │   ├── test_mark_parametrize.py
│   │   ├── test_fixtures.py
│   │   ├── test_fixtures_scope.py
│   │   ├── test_chained_fixtures.py
│   │   ├── test_mock.py
│   │   └── test_patch.py
│   │
│   └── conftest.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# ▶️ Cómo ejecutar los tests

Ejecutar todos los tests

```bash
pytest
```

Modo detallado

```bash
pytest -v
```

Mostrar la salida de `print`

```bash
pytest -s
```

Ejecutar un archivo específico

```bash
pytest learning_exercises/tests/test_fixtures.py
```

Ejecutar un único test

```bash
pytest learning_exercises/tests/test_fixtures.py::test_validar_numero
```

Ejecutar por marcador

```bash
pytest -m smoke
```

---

# 🎯 Conceptos practicados

- ✅ Assertions
- ✅ Fixtures
- ✅ Fixture Scope
- ✅ Chained Fixtures
- ✅ Parametrize
- ✅ Marks
- ✅ Mock
- ✅ Patch
- ✅ Yield Fixtures
- ✅ Setup & Teardown
- ✅ Factory Fixtures
- ✅ Objetos personalizados
- ✅ Colecciones
- ✅ Ejercicios tipo entrevista

---

---

# 💼 Objetivo profesional

Este repositorio forma parte de mi preparación como **QA Automation Engineer**, donde practico conceptos fundamentales y avanzados de **Pytest** aplicados a escenarios reales, con el objetivo de escribir pruebas limpias, reutilizables, mantenibles y alineadas con las buenas prácticas de la industria.

---

# ⭐ Si este repositorio te resulta útil

Si este contenido te ha servido como guía para aprender Pytest o QA Automation, considera dejar una ⭐ al repositorio.
