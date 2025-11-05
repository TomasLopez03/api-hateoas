# 🚀 API con HATEOAS

Esta API simula una compra, donde se pueden ver los productos, agregarlos al carrito, 
generar la orden del carrito y pagar la orden o cancelarla.

------ 

# 📝 Caracteristicas
* **HATEOAS implementado:** Los recursos incluyen **enlaces (_links)** que guían al consumidor sobre
  las acciones disponibles.
* **Diseño Limpio:** Estructura de código clara y facil de mantener.

------

# ⚙ Requisitos previos
Asegúrate de tener instalado lo siguiente:
* Python 3.13.7
* Git
* pip (para manejar dependecias)

------

# 🛠 Configuración y Ejecución Local
**1. Clonar Repositorio**

Abre tu temrinal y ejecuta lo siguiente:
```
  git clone https://github.com/TomasLopez03/api-hateoas.git
  cd api-hateoas
```
**2. Instalar Dependecias**
* Si tienes **virtualenv** lo mejor seria activarlo para evitar errores con las dependecias, 
si no lo tienes sigue estos pasos:
  1. En tu terminal ejecuta:
     ```
       pip install virtualenv
     ```
  2. Dentro del repositorio api-hateoas crea el entorno ejecutando:
     ```
       python -m venv venv
     ```
  3. Activa el entorno:
     ```
       ./venv/scripts/activate
     ```
  4. Por ultimo instala las depencias:
     ```
        pip install -r requeriments.txt
     ```

**3. Preparar la base de datos (Migraciones)**

Instaladas las dependencias, debes aplicar las migraciones para crear la estructura de la base de datos,
Django por defecto usa SQLite3 asi que no te preocupes:
* Ingresa a la carpeta principal:
```
  cd hateoas
```
* Crear archivos de migración:
```
  python manage.py makemigrations
```
* Aplica las migraciones a la base de datos: 
```
  python manage.py migrate
```

**4. Ejecutar la API**

Ejecuta el script de inicio:
```
  python manage.py runserver
```
Deberías ver un mensaje en la consola indicando que el servidor se ha iniciado, 
probablemente en http://localhost:8000

------

# Documentacion (Swagger)

Para ver la documentacion y explorar la api, a la url: 
http://localhost:8000/api/schema/swagger-ui/

Para apresiar mejor el funcionamiento de HATEOAS puedes ir a Postman con la url base:
* GET http://localhost:8000/api/ : Te proporcionara **/productos** para empezar a navegar
* POST **URLBase/productos**: Puedes cargar una lista de productos para poder probrar las funciones

# 🤝🏻Contribuciones
Si encuentras un erro o tienes alguna sugerencia, siente libre de abrir un issue o enviar una pull request







