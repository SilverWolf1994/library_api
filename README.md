Library API

Este proyecto fue generado usando FastAPI, SQLAlchemy, Pytest & MySQL.


-Utiliza los siguientes comandos en orden para hacer un correcto uso del proyecto.

Crear & Activar Entorno Virtual:
library_api> py -m venv virtual
library_api> .\virtual\Scripts\activate

Iniciar Aplicación:
library_api> uvicorn app.main:app

Iniciar Tests:
library_api> pytest


-Base de Datos:

Cambiar los datos de conexion en el archivo de la ruta: app/config/database.py por los datos de tu entorno.
Crear base de datos: library
Importar el archivo: library.sql


-Librerias:

Instalar las librerias que se encuentan en el archivo requirements.txt.
library_api> pip install -r requirements.txt
