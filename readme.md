# Entrega Final - Blog en Django

¡Hola! Soy Martín Castro y este es mi proyecto final para el curso de Python/Django. Se trata de una aplicación web tipo blog desarrollada de forma individual. El objetivo principal fue aplicar todos los conceptos aprendidos en el curso: manejo de usuarios, perfiles, autenticación, herencia de templates, manejo de imágenes, mensajes entre usuarios, y más.

## Descripción general

La aplicación permite a los usuarios registrarse, iniciar sesión, editar su perfil (incluyendo avatar y biografía), crear páginas/entradas de blog con texto enriquecido (gracias a CKEditor) e imágenes, editar o borrar sus publicaciones, y enviar mensajes privados a otros usuarios. Además, cuenta con una sección "Acerca de mí" y una navegación intuitiva desde el NavBar.

## Funcionalidades principales

# Video
    
    https://drive.google.com/file/d/1fs6tEYK7-_x6-5TQm-I7JhsmCPIzs4Y6/view?usp=sharing



- Registro de usuario con username, email y password.
- Login y logout seguro.
- Perfil de usuario editable (nombre, apellido, email, avatar, biografía, fecha de nacimiento).
- Vista "Acerca de mí" (about/).
- Listado de páginas/entradas (pages/) y detalle de cada una.
- Creación, edición y borrado de páginas solo para usuarios logueados.
- Editor de texto enriquecido (CKEditor) e imágenes en las publicaciones.
- Mensaje de aviso si no hay páginas aún o si la búsqueda no arroja resultados.
- Mensajería entre usuarios.
- Herencia de templates y NavBar visible en todas las páginas.
- Uso de CBVs, mixins y decoradores para manejo de permisos.
- Todas las apps y modelos registrados en el admin de Django.

## Estructura del proyecto

- **accounts**: Gestión de usuarios (registro, login, logout, perfil, edición, cambio de contraseña).
- **pages**: Manejo de páginas/entradas del blog (CRUD).
- **messenger**: Envío y recepción de mensajes privados entre usuarios.
- **static**: Archivos estáticos (CSS, imágenes del sitio).
- **media**: Archivos subidos por los usuarios (imágenes de perfil y publicaciones, ¡no está en el repo!).
- **templates**: Templates base y herencia.
- **README.md**: Este archivo.
- **requirements.txt**: Dependencias del proyecto.
- **.gitignore**: Para evitar subir archivos no deseados.

## Instalación y ejecución

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/MartinCastr0/Entrega-final-MartinCastro.git
    cd Entrega-final-MartinCastro
    ```

2. **Crear y activar un entorno virtual**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate     # En Windows
    ```

3. **Instalar las dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar variables de entorno (opcional)**
    - Revisar el archivo `settings.py` para la configuración de base de datos, correo, etc.

5. **Realizar migraciones**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Crear un superusuario**
    ```bash
    python manage.py createsuperuser
    ```

7. **Levantar el servidor de desarrollo**
    ```bash
    python manage.py runserver
    ```

8. **Acceder a la app**
    - Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

## Notas importantes

- **No subí la base de datos (`db.sqlite3`) ni la carpeta `media/` al repo.** Ambos están en `.gitignore` para asegurar privacidad y evitar archivos pesados en el control de versiones.
- **Las imágenes de los usuarios y publicaciones van en `media/`, no en `static/`.**
- **Si agregás librerías nuevas, no te olvides de actualizar `requirements.txt` con `pip freeze > requirements.txt`.**

## Requisitos cumplidos

- Herencia de templates y NavBar en el base.
- Manejo de imágenes en formularios y modelos.
- Uso de CKEditor para campos enriquecidos.
- Uso de CBVs (Class Based Views) y mixins para permisos.
- Decoradores en vistas comunes.
- Apps separadas para autenticación y mensajería.
- Mensajes de aviso si no hay datos.
- README completo y explicativo.
- Video demostración (ver en la entrega).

## Créditos

Proyecto realizado por **Martín Castro** como entrega final para el curso de Python/Django.

---

¡Gracias por revisar mi proyecto! Si tenés sugerencias o encontrás algún error, no dudes en contactarme.


