#Sprint 9 Lab 1

En esta practica tenemos que hacer una calculadora y ejecutar test unitarios como  pipeline en Github action, esa ejecucion se llevara acabo automaticamente cuando ejecutemos algun push.

##Para poder ejecutar nuestro pipeline tenemos que seguir esta estructura de carpetas


├───.git # carpeta por defecto de git
│   ├───hooks
│   ├───info
│   ├───refs
│   │   ├───heads
│   │   ├───tags
│   │   └───remotes
│   │       └───origin
├───.github
|    └───workflows
|        └───ci.yml # fichero encargado de configurar y ejecutar nuestro pipeline
├───operaciones.py # fichero donde declaramos que operaciones ha de realizar nuestra app/calculadora
└───test_operaciones.py # fichero donde declaramos los test (en unittest) que nuestro pipeline ha de realizar.

Aunque lo mas relevante aqui es ver que funcione nuestro pipeline, dentro de cada fichero tendremos una mini explicacion de que hace cada cosa.

Para comprobar las operaciones se ejecuta el comando:
		python3 operaciones.py
	Para comprobar los tests, se ejecuta el comando: 
		python3 test_operaciones.py
	
	Una vez modificados los archivos 'operaciones.py', 'test_operaciones.py' y 'ci.yml' (Actions) se sincroniza en 
	GitHub ejecutando los comandos:
		git commit -am "Actualizacion de los ficheros operaciones y test_operaciones" 
		git push

Con esto nuestro pipeline deberia estar funcionando automaticamente, podremos ver en la pestana de Actions, hubicado encima del nombre de nuestro repositorio.
