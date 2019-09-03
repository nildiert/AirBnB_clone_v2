# Flask

[![N|Solid](https://miro.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png)](https://palletsprojects.com/p/flask/)


Flask es un microframework minimalista escrito en [Python](https://es.wikipedia.org/wiki/Python) que permite crear aplicaciones web rápidamente y con un mínimo de lineas de código.

# Instalación Python3
 Puedes verificar si tienes instalado python en versiones linux con el siguiente comando:
 ```sh
   python3 -v
```
  Si eres usuario de ubuntu o debian puedes instalar python con el siguiente código:
```sh
  sudo apt-get update
  sudo apt-get install python3.1
```
Si eres usuario de Red Hat o Centos por ejemplo puedes usar estos comandos para instalar python:
```sh
  sudo apt-get update
  sudo yum install python
```
Si usas Windows o Mac, puedes buscar como instalar python dando click [aquí](https://tutorial.djangogirls.org/es/python_installation/).

# Instalación Flask

Instala flask con este comando:
```
  sudo pip3 install flask
```
Puedes verificar si flask se encuentra instalado con el comando:
```
   sudo pip3 freezeflask
```

# Hello World en Flask:

Debido a que en muchas maquinas vas a necesitar crear el entorno de desarrollo de flask, es recomendable que crees un archivo `requirements.txt` y dentro coloques todas las dependencias de flask que vas a necesitar.
```
flask git:(master) ✗ cat requirements.txt
flask
```
Después de tener tú archivo de requirements, puedes instalar todas las dependencias de flask de tú proyecto con el comando:

```
  sudo pip install -r requirements.txt
```

Una vez tienes instalado Flask puedes crear tú primer Hello World ...

Crea un archivo `main.py` y coloca dentro este texto
```
from flask import Flask

@app.route('/')
app = Flask(__name__)
def hello():
    return 'Hello World Flask'
```

Crea una variable de entorno con el archivo que acabas de crear
```
export FLASK_APP=main.py
```
Listo! Ahora puedes ejecutar tu aplicación de flask:
```
flask run
```

Esto te va a arrojar una dirección para que hagas tus desarrollos (`http://127.0.0.1:5000/`), si entras en tu navegador a esa dirección, encontrarás el texto "Hello World Flask".


# Debugging mode:

Con el modo de debugging, no tienes que prender y apagar el servidor para verificar los cambios, basta con que solo refresques la pagina.

Para habilitar el modo de debugging, apaga el servidor y crea la siguiente variable de entorno:

```
export FLASK_DEBUG=1
```
Ejecuta de nuevo el servidor:
```
flask run
```

# Development mode:

Creamos la siguiente variable de entorno
```
export FLASK_ENV=development
```

y reiniciamos el server de flask
```
flask run
```

# Testing:

Para realizar tests en flask, debes exportar la variable de entorno

```
export FLASK_APP=main.py
```
y correr el siguiente comando:

```
flask test