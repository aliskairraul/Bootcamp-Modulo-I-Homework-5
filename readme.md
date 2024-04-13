# Stack Excercise Homework 5

<p style="text-indent: 40px;">Este repositorio está dedicado a compartir los algoritmos realizados en el Homework 5 del Modulo I del Bootcamp de Henry en la especialidad de Data Science.  <br></p>
<p style="text-indent: 40px;">El Homework consta de 2 Juegos  <br></p>

- Juego de 20 Cartas<br>
  Implementar un juego, que consista en apilar números enteros del 1 al 20, de forma aleatoria, para lo cual debe usarse una estructura de Pila.
  Luego, el usuario debe elegir un número de veces en que se va a quitar elementos de la pila, los cuales, sumados entre sí, no deben superar el valor de 50.
  El usuario pierde si la suma supera ese valor. Si no lo supera, gana, pero su calificación será 10 menos el número elementos que falten quitar para todavía no superar 50.
  El programa debe informar si perdió, y si ganó, con qué calificación lo hizo.
- Juego de 2 Contenedores<br>
  Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L.
  Las opciones posibles son:
  - Llenar la jarra de 3 litros
  - Llenar la jarra de 5 litros
  - Vaciar la jarra de 3 litros
  - Vaciar la jarra de 5 litros
  - Verter el contenido de la jarra de 3 litros en la de 5 litros
  - Verter el contenido de la jarra de 5 litros en la de 3 litros

<p style="text-indent: 40px;">Los archivos en el repositorio para el cumplimiento del Homework son los siguientes:  <br></p>

- stack_cards.py --> Estructura de Datos que se usa en el juego de 20 cartas
- stack_containers.py --> Estructura de Datos que se usa en el juego de las 2 jarras
- utiles.py --> Contiene una Clase **Utiles** que tiene metodos para limpiar pantalla, insertar lineas en blanco, incializar logger para llevar registro de los juegos, etc

- twenty_card.py --> Contiene la lógica del juego de 20 cartas
- two_containers.py --> Contiene la lógica del juego de las 2 jarras
- main.py --> archivo a correr que inicia la aplicación

### Uso:

<p style="text-indent: 40px;">Abrir la terminal y ubicarse en la carpeta donde descargue el repositorio. Una vez ubicado en la carpeta ejecutar el archivo <b>main.py</b>  <br></p>
<image src='images/corriendo_main.png'>
<p style="text-indent: 40px;">Una vez ejecutado debe aparecerle la siguiente pantalla que es el menu principal<br></p>
<image src='images/menu_principal.png'>
<p style="text-indent: 40px;">Seleccionando la opcion 1, entra al juego de cartas donde selecciona la cantidad de cartas a repartir<br></p>
<image src='images/numero_cartas.png'>
<p style="text-indent: 40px;">Al seleccionar el numero de cartas se muestra una pantalla parecida a la siguiente donde se calcula la puntuación del jugador según lo enunciado en el ejercicio<br></p>
<image src='images/juego1_final.png'>
<br>
<br>
<p style="text-indent: 40px;">Sí en el menú inicial selecciona la opción 2 para jugar el juego de las Jarras, cae en la siguiente pantalla<br></p>
<image src='images/juego_jarras.png'>
<p style="text-indent: 40px;">Debe seguir las instrucciones planteadas en este archivo cuando se habla del juego de las jarras. Y de obtener la solución verá algo como lo siguiente:<br></p>
<image src='images/juego2_final.png'>

### Autor:

Aliskair Rodríguez<br>
Henry Bootcamp Data Science<br>
Cohorte Data-PT10
