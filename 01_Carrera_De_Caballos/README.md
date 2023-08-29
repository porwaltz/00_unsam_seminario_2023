#Carrera de caballos

Implementar una "carrera de caballos" usando threads, donde cada "caballo" es un Thread o bien un objeto de una clase que sea sub clase de Thread 
y contendrá una posición dada por un número entero. El ciclo de vida de este objeto es incrementar la posición en variados instantes de tiempo, 
mientras no haya llegado a la meta, la cual es simplemente un entero prefijado. Una vez que un caballo llegue a la meta, se debe informar en 
pantalla cuál fue el ganador, luego de lo cual los demás caballos no deberán seguir corriendo. Imprimir durante todo el ciclo las posiciones de 
los caballos, o bien de alguna manera el camino que va recorriendo cada uno (usando símbolos Ascii). El programa podría producir un ganador disitnto cada vez que se corra. Opcionalmente, extender el funcionamiento a un array de n caballos, donde n puede ser un parámetro.