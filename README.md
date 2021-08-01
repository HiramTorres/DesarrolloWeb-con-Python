# Desarrollo web con python
Para este proyecto utilizaré el microframework **Flask** 


### Para utilizar Flask
Previamente, instalaré y utilizaré  **Virtualenv**, que es una herramienta para  generar entornos para proyectos y tenerlos aislados unos de otros y evitar conflictos con versiones de librerías etc. 

### Instalación 
```pip install virtualenv``` 
- Descargará todo el contenido


y una vez este instalado, se crea un entorno utilizando desde la terminal los comandos: 
> virtualenv -p "version de python" "Nombre del entorno"

Ejemplo:

```virtualenv -p python3 env ```

Una vez hecho, se crea un folder en la ruta de archivos asignada previamente 

### Para iniciar el entorno 
Debemos ingresar el comando desde consola de: 
> source ""Nombre del entorno"/bin/activate 

Ejemplo:
```source env/bin/activate```

y listo el entorno esta en ejecución, ahora todas las librerías quedarán instaladas en el entorno aislado de lo demás. 

### Para detener el entorno

>Ejecutamos: ``` diactivate```
 
y listo, el entorno se detuvo.

----------------------------

### Para instalar Flask

Utilizamos el comando directo en consola de: 
```pip install flask```

Esperamos a que se descarguen todos los contenidos y corroboramos utilizando el shell de python desde la terminal

``` 
~python
import flask
```
Sí no genera ningún error, eso quiere decir que la instalación fue hecha correctamente. 

--------------------------


### Creación de un servidor 
Para crear un servidor tenemos que crear una carpeta desde donde trabajar y abrir el editor de texto que en mi caso es Visual Studio Code

Una vez abrierta la carpeta se crea un archivo nuevo que llamaré ```main``` y tendra una extensión ```.py```

Una vez hecho eso importaremos la clase Flask dentro de la librería de flask 

```from flask import Flask```

y realizaremos una instancia 
```app = Flask(__name__)```
>Entre los parentesis se pone el argumento como contexto en este caso ```name```

y untilizaremos la condición 
```
if __name__ == '__main__':
    app.run()
```
Y con estas líneas de código se genera el servidor y se levanta

Cuando el código esté listo, se guarda y desde la terminal se ejecuta el archivo

```python main.py```
y la terminal te abrirá una ruta desde el local host para visualizar tus cambios y quedará a la escucha desde el puerto 5000 

Si queremos que el archivo este en algún otro puerto solo basta con modificar el parametro ```port``` del método ```run```

```
if __name__ == '__main__':
    app.run(port=9000)
```

y actualizando obtendremo la misma salida.

De aquí en adelante nos encontramos en una fase de desarrollo, por lo que en el método run podemos modificar el parámetro ```debug``` como verdadero para indicar a servidor que estamos en una etapa de desarrollo ya que los errores pueden sucitarse y que si algo falla el servidor pueda indicar cual fue el error 

``` 
if __name__ == '__main__':
    app.run(debug=True,port=9000) 
```

--- 
Para que nuestro servidor este listo para las peticiones de los diferentes clientes debemos asignarle una ruta especifica 

Después de generar la instancia ```app``` se crea la ruta utilizando 
```
@app.route('/') 
```
Este metodo recibe obligatoriamente un argumento que será un string
e iniciamos con el index por eso el slash / 

generamos una nueva función la cual llamaré ```index```
```
def index():
    return "Hola Mundo desde el servidor de Hiram!"
```

Cada cambio que se haga en el scrip se estará actualizando automaticamente en el servidor solo hace falta actualizar la página del navegador y listo 

--- 
### Renderizar template 
Se debe renderizar un archivo html para que sea más completo el file y solo lo renderice el servidor 
y se pueda visualizar en el navegador 



Se hace un nuevo folder llamado "templates" y ahí colocamos el archivo html para que sea renderizado 

Posteriormente importamos la funcion de ```render_template```

```
from flask import render_template
``` 

una vez importado nos colocamos en el código de la funcion index y retornamos ```render_templates```

Y esta funcion recibe como argumento el nombre del archivo a renderizar 
```
return render_template('templates/index.html')
```
