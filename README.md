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

```from flask import render_template``` 

una vez importado nos colocamos en el código de la funcion index y retornamos ```render_templates```

Y esta funcion recibe como argumento el nombre del archivo a renderizar 
``` return render_template('templates/index.html')```

---
### Ciclos y condicionales 

Para generar una condición se genera una nueva variable 

``` premium = True```

y se agrega dentro de los parametros

```
return render_template("index.html",username=name,lastname=lname,premium=premium)
```
Generamos una nueva etiqueta en el index.html
```
<p>
    La página web es premium
</p>
```
Para generar una condición en el template lo hacemos de la siguiente forma 
```
{% if premium %}


{% endif %}
``` 
>Se debe terminar con unas llaves de cierre porque la identación no funciona en los archivos html

Dentro de los condicionales se pueden utilizar los operadores lógicos y ariméticos 

Al igual de que se puede utilizar un ```else``` dentro del condicional 

```
{% if premium %}
    <p>
        La página web es premium.
    </p>
{% else %}
    <p>
        La página es visible para todo el mundo
    </p>

{% endif %}
``` 
Y también se pueden utilizar ```if``` anidados .

#### Ahora utilizaré un ciclo For en el archivo .html

Generaré una nueva variable llamada skill 
```
skills = [Python, Java, C, HTML]
```
y quiero utilizar esto como un parámetro 

```
return return render_template("index.html",username=name,lastname=lname,premium=premium, skills = skills)
```

Voy a condicionar si la lista posee elementos para mostrar

```
{% if skills %}
    <p>listado de skills</p>
    <ul>
        {% for skill in skills: %}
            <li> {{ skill }} </li>
        {% endfor %}    
    </ul>

{% endif %}



```

#### Plantillas Jinja2
Flask utiliza el motor de templates (platillas) Jinja2 , este es, quizás, una de las librerías más populares de Python, con ella podemos generar documentos HTML de una forma rápida y sencilla.

Al trabajar con Jinja2 debemos tener presentes 3 elementos importantes:
* Variables ```{{ variable}}```
* Instrucciones ```{% instrucción %}```
* Comentarios ```{# comentarios #}```

El único ciclo permitido por *Jinja 2* es el ciclo **for**

Dentro del ciclo podemos acceder a diferentes atributos del objeto loop.
* index: Interacción actual. El valor comienza en 1
* index0: Iteración actual. El valor comienza en 0 (Ideal si deseamos replicar el comportamiento de la función enumerate)
* first: Valor verdadero si nos encontramos en la primera iteración.
* last: Valor verdadero si nos encontramos en la última iteración.
* length: Número de iteraciones.

**Ejemplo:**
```
<ul>
    {% for val in [1,2,3,4,5,6,7,8,9] %}
        <li> {{ loop.index0 }} - {{ val }} </li>
    {% endfor %}
</ul>    
```
#### FUNCIONES
Aunque la integración de Flask y Jinja2 nos permite ejecutar ciertas funciones y métodos dentro de nuestro template, habrá ocasiones en las que necesitemos utilizar funciones propias, en esos casos lo que podemos hacer es enviar las funciones al template a través de la función render template.
```
def suma(val1, val2):
    return val1 + val2

def suma_template():
     return render_template('suma.html', val1=10, 
                                         val2=30, funcion=suma)
```

```
<p>
La suma de {{ val1 }} + {{ val2 }} es : {{ funcion(val1, val2) }}
</p>
```
--- 
### Parámetros 
Para poder generar URLs de forma dinámicas podemos utilizar los parámetros de la siguiente forma: 
```
@app.route('/usuario/<username>')
def usuario(username:
    return 'Hola' + username
```
>Utilizamos los signos de más y menos para identificar el nombre del parámetro con el que trabajaremos 

y despues el parámetro se le da a la función. 

--- 
### Archivos estáticos 
Son los archivos css,Javascript etc. 

Crearemos una nueva carpeta la cual debe tener el nombre de 'static', y dentro de esta carpeta pondremos todos nuestros archivos Css, JavaScrip o imágenes en sus respectivas carpetas. 

Dentro de mi archivo .html colocaré una sección de ```<link>``` para de ahí jalas nuestros estilos css ya guardados dentro del archivo correspondiente. Todo eso de la siguiente forma: 

```
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
```

y así podemos dar formato a nuestro archivo html. 

--- 
Ahora crearé una referencia para el archivo java script. 
Para importar ese archivo Javascript colocamos un ```<script>``` en el archivo html de esta forma: 
```
<script type="text/javascript" scr="{{ url_for('static', filename='js/scripts.js') }}" >
```
