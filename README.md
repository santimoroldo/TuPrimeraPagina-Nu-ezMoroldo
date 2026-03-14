# Adsum Tech - Entrega Proyecto Python
**Estudiante:** Santiago Nuñez Moroldo  
**Curso:** Python & Django - Coderhouse

## 🚀 Descripción del Proyecto
Este es un sistema de gestión para un blog tecnológico desarrollado con el patrón **MVT (Model-View-Template)** de Django. La plataforma permite administrar autores, secciones y publicaciones técnicas de manera eficiente.

## 🛠️ Tecnologías utilizadas
* **Python 3.14**
* **Django 6.0.3**
* **Bootstrap 5** (Estilización y Layout)
* **SQLite** (Base de Datos)

## 📋 Funcionalidades
El proyecto cumple con todos los requisitos solicitados en la entrega:
1. **Modelos:** Implementación de clases para `Autor`, `Seccion` y `Post`.
2. **Formularios:** Tres formularios funcionales para la carga de datos en la base de datos.
3. **Búsqueda:** Un motor de búsqueda que permite filtrar autores por nombre y devuelve su contacto.
4. **Herencia de Templates:** Uso de un archivo `padre.html` para unificar la estética del sitio.
5. **Mensajes de éxito:** Feedback visual al usuario tras cargar información correctamente.

## ⚙️ Instrucciones de uso
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv env`.
3. Activar el entorno: `.\env\Scripts\activate`.
4. Instalar Django: `pip install django`.
5. Ejecutar migraciones: `python manage.py migrate`.
6. Iniciar el servidor: `python manage.py runserver`.
7. Navegar a: `http://127.0.0.1:8000/blog/`.

## 📂 Estructura del repositorio
* `/blog`: Aplicación principal con modelos, vistas y formularios.
* `/templates`: Carpeta de plantillas HTML con sistema de herencia.
* `db.sqlite3`: Base de datos con datos de prueba cargados.
* `manage.py`: Script de administración de Django.
