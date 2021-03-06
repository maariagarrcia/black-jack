#
# P A G I N A S   C O N S U L T A D A S
#
# Tipo de Datos: List ............... https://www.w3schools.com/python/python_lists.asp
# Tipo de Datos: Dictionary ......... https://pythonexamples.org/python-dictionary-operations/
#
# Método de Random "choice()" ....... https://www.w3schools.com/python/ref_random_choice.asp
# Método de Random "sample" ......... https://www.w3schools.com/python/ref_random_sample.asp
# Método de String "join()".......... https://www.w3schools.com/python/ref_string_join.asp
#
# Función "format()" ................. https://www.w3schools.com/python/ref_func_format.asp
# Función "sorted()" ................ https://www.w3schools.com/python/ref_func_sorted.asp
# Función "sum()"  ................... https://www.w3schools.com/python/ref_func_sum.asp
#

# D E S C R I P C I O N     T A R E A    R E A L I Z A D A:
#
# 0) Estudiar el código suministrado en la tarea 
# 1) Buscar documentación sobre los tipos de datos, funciones y métodos que se van a necesitar
# 2) Crear un nuevo código usando lo aprendido previamente:
#       · Hacer un código lo más legible posible
#       · Hacer el código lo más modular posible usando funciones (no se requieren módulos)
# 3) Documentar la tarea realizada sobre el propio código para facilitar el estudio posterior
#
#

from random import choice, sample
from colorama import Fore
import operator

# En este diccionario se guardan las cartas y su puntuación
cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

#
#  F U N C I O N E S
#

def mostrarCartas():
    print(Fore.YELLOW + "--- Baraja ordenada por puntuaciones ---")
    cartasOrdenadas=  sorted(cartas.items(), key=operator.itemgetter(1))
    for key, value in cartasOrdenadas:
        print ("(" +key+ " " + str(value) +") ", end="")
     
    print()
    print()



def mostrarReglasJuego():
    # Preparativos antes de empezar la partida
    print(Fore.LIGHTYELLOW_EX)
    print()
    print(" B l a c k j a c k")
    print("====================")
    print(" Hola, soy el ordenador y vamos a jugar al blackjack (21)")
    print(" Vamos a jugar de la siguiente forma (según enunciado práctica)") 
    print(" 1) El jugador escogerá 2  cartas a su gusto")
    print(" 2) El ordenador escogerá dos cartas al azar")
    print(" El que se aproxime mas a 21 sin pasarse gana!!!")
    print()

def turnodelJugador(listaCartas):
    # Seleccionar la PRIMERA carta del jugador
    print(Fore.WHITE + " El jugador ha seleccionado:", end=" " )
    carta_1= choice(listaCartas)
    print(carta_1, end= " " )

    # Seleccionar la SEGUNDA carta del jugador
    carta_2= choice(listaCartas) 
    print(carta_2, end= " " )
    
    # Calcular y devolver la puntuación del jugador
    puntuacion= cartas[carta_1] + cartas[carta_2]
    print(" >>> su puntuacion es de"+ Fore.RED, puntuacion)
    return puntuacion

def turnoBanca(listaCartas):
    # Seleccionar dos cartas aleatoriamente a la vez 
    # El metodo sample() selecciona "n" items de una lista y los devuelve
    # en otra lista. En nuestro caso le pedimos que seleccione 2 items.
    cartas_banca= sample(listaCartas, 2)
    
    # Calcular y devolver la puntuación de la banca
    puntuacion= sum(cartas[carta] for carta in cartas_banca)
    print(
        (Fore.WHITE + "La banca tiene: {} {} >> su puntucioó es" + 
        Fore.RED + "{}").format(cartas_banca[0],cartas_banca[1], puntuacion)
    )

    return puntuacion
   
def mostrarGanador(puntosJugador, puntosBanca):
    # Esta funcion aunque el enunciado no lo piide muestra el ganador!
    # Sacando solo dos cartas en realidad no9 hay forma de pasarse de 21
    # pero igualmente lo he contemplado
    print(Fore.WHITE, end= " " )
    if puntosJugador>21:
        print("El jugador se ha pasado de 21 >>>> " + Fore.RED + "La banca gana")
    elif puntosBanca>21:
        print(" La banca se ha pasado de 21 >>>" + Fore.RED + "El jugador gana" )
    elif puntosJugador>puntosBanca:
        print("El  jugador ha conseguido mejor puntuacion")
    else:
        print(" La banca ha conseguido mejor puntuacion >>>" + Fore.RED + " La banca gana" )



    print(Fore.YELLOW + "--- LA PARTIDA HA FINALIZADO --- ")
    print()

def jugar():
    # Crear una lista a partir del diccionario que contiene las cartas
    # Se necesita una lista para luego poder usar el metodo choice() y también el sample
    # que no funcionan directamente sobre diccionarios sino sobre listas
    lista_cartas= list(cartas)

    puntosJugador = turnodelJugador(lista_cartas)
    puntosBanca = turnoBanca(lista_cartas)

    # A esta  función le pasamos  las puntuaciones respectivas para que pueda
    # "decidir" quien ha sido el ganador
    mostrarGanador(puntosJugador,puntosBanca)

    

#
#
#  I N I C I O    P R O G R A M A
#
#
mostrarReglasJuego()
mostrarCartas()

print(Fore.WHITE + "--- Inicio Partida ---")
jugar()
print(Fore.WHITE + "--- Fin Partida ---")
