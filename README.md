# TuPrimeraPaginaCastro

Proyecto Django de ejemplo para practicar el patrón MVT, herencia de plantillas, modelos, formularios y búsqueda en la base de datos.

## Pasos para probar la aplicación

1. **Clona el repositorio:**
   ```
   git clone https://github.com/TuUsuario/TuPrimeraPaginaCastro.git
   cd TuPrimeraPaginaCastro
   ```

2. **Instala dependencias y realiza migraciones:**
   ```
   python manage.py migrate
   ```

3. **Levanta el servidor:**
   ```
   python manage.py runserver
   ```

4. **Funcionalidades:**
   - Desde la barra de navegación puedes:
     - Crear autores (`Nuevo Autor`)
     - Crear categorías (`Nueva Categoría`)
     - Crear entradas de blog (`Nueva Entrada`)
     - Buscar entradas por título (`Buscar Entrada`)
   - La plantilla base (`base.html`) es heredada por todas las páginas.
   - Cada modelo tiene su propio formulario de carga.
   - La búsqueda se realiza por título de entrada.

## Orden sugerido para probar

1. Crear uno o más autores.
2. Crear una o más categorías.
3. Crear entradas, seleccionando autor y categoría.
4. Buscar entradas por título.

¡Listo! Cumple con todos los requisitos de la consigna.