# Requerimientos del sistema
- python 3
- pip 3
- django 2.2
- djangorestframework última version
- git (para traer el código del repositorio)

# Instalación
- Crear carpeta para el proyecto
- Ingresar en la carpeta
- Clonar el repositorio:
    git clone https://github.com/daniel9610/ApiDjango.git .
- Crear base de datos y agregar su configuración en el archivo ApiDjango/settings.py
- Ejecutar las migraciones.
- Llenar la base de datos (sé que debí hacerlo con seeds pero no me alcanzó el tiempo).

# End-Points
* Las inserciones desde el api se pueden hacer con los formularios de djangoRestFramework, si desean hacerlo desde url también se puede hacer.

# Clientes
- http://localhost:puerto/clients:              Lista todos los clientes
- http://localhost:puerto/clients/{id}:         Lista un cliente en específico
- http://localhost:puerto/clients-csv:          Descarga archivo csv con todos los clientes

# Productos
- http://localhost:puerto/products:              Lista todos los productos
- http://localhost:puerto/products/{id}:         Lista un producto en específico
- http://localhost:puerto/products-csv:          Descarga archivo csv con todos los productos

# Facturas
- http://localhost:puerto/bills:              Lista todas las facturas
- http://localhost:puerto/bills/{id}:         Lista una factura en específico
- http://localhost:puerto/bills-csv:          Descarga archivo csv con todas las facturas

# Facturas por productos
- http://localhost:puerto/bills-products:              Lista las facturas por productos
- http://localhost:puerto/bills-products/{id}:         Lista una relación de factura por producto
- http://localhost:puerto/bills-products-csv:          Descarga archivo csv con todas las facturas por productos

