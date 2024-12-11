# Library API

Este proyecto fue creado usando FastAPI, SQLAlchemy, Pytest & MySQL.<br/><br/>


# Crear & Activar Entorno Virtual:<br/>
library_api> py -m venv virtual<br/>
library_api> .\virtual\Scripts\activate<br/><br/>

# Iniciar Aplicación:<br/>
library_api> uvicorn app.main:app<br/><br/>

# Iniciar Tests:<br/>
library_api> pytest<br/><br/>


# Base de Datos:<br/>

Cambiar los datos de conexión en el archivo de la ruta: app/config/database.py por los datos de tu entorno.<br/>
Crear base de datos: library<br/>
Importar el archivo: library.sql<br/><br/>


# Librerias:<br/>

Instalar las librerías que se encuentran en el archivo requirements.txt.<br/>
library_api> pip install -r requirements.txt
