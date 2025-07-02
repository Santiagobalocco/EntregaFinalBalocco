# Blog_oficial - Proyecto Final Python Django

Este proyecto es un blog desarrollado como entrega final del curso de Python con Django. Permite a los usuarios registrarse, iniciar sesión, publicar contenido, editar su perfil y enviar mensajes a otros usuarios.

## Funcionalidades

 **Sistema de usuarios(accouts)**  
- Registro con nombre de usuario, email y contraseña  
- Login / Logout  
- Edición de perfil con imagen (avatar), biografía y fecha de nacimiento  
- Cambio de contraseña  

 **Paginas (Pages)**  
- Crear publicaciones con título, subtítulo, contenido (formato enriquecido con CKEditor) e imagen  
- Ver lista de publicaciones  
- Leer publicación completa  
- Editar y eliminar publicaciones propias  
- Búsqueda de publicaciones  
- Aviso si no hay publicaciones disponibles  

 **Acerca de mí (About)**  
- Vista con biografía del autor del blog  

 **Mensajería entre usuarios(Messenger)**  
- Enviar mensajes privados a otros usuarios registrados  
- Bandeja de entrada y enviados

## Tecnologías utilizadas

- Python 3  
- Django 4  
- Bootstrap 5 (via CDN)  
- SQLite  
- CKEditor  
- HTML + CSS  
- Git + GitHub  

## Instalación y ejecución

1. Clonar el repositorio  
```bash
git clone https://github.com/tuusuario/nombre-del-repo.git
cd nombre-del-repo
```

2. Crear entorno virtual y activarlo  
```bash
python -m venv .venv
.venv\Scripts\activate   # en Windows
```

3. Instalar dependencias  
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones y correr el servidor  
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. Acceder en tu navegador a `http://127.0.0.1:8000/`

## 

Incluye vistas de:  
- Inicio  
- Login y Registro  
- Perfil de usuario  
- Edición de perfil  
- Publicaciones  
- Envío de mensajes  

## Notas importantes

- No se incluye el archivo `db.sqlite3` por estar ignorado en `.gitignore`  
- Las imágenes de usuarios (avatar) se suben a `/media/`  
- Las imágenes y archivos del código se encuentran en la carpeta `static/`  

## Autor

Santiago Balocco  
Curso Python con Django - Proyecto final

## Video de youtube mostrando todas las funcionalidades

