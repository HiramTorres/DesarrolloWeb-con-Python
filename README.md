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

