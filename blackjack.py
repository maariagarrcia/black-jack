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
# Funcion "format()"................. https://www.w3schools.com/python/ref_func_format.asp
# Funcioon "sorted()"................ https://www.w3schools.com/python/ref_func_sorted.asp
# Funcion "sum()" ................... https://www.w3schools.com/python/ref_func_sum.asp
#

# D E S C R I P C I O N     T A R E A    R E A L I Z A D A:
#
# 0) Estudiar el código suministrado en la tarea 
# 1) Buscar documentación sobre los tipos de datos, funcions y métodos que se van a necesitar
# 2) Crear un nuevo código usando lo aprendido previamente:
#       · Hacer un código lo más legible posible
#       · Hacer el código lo más modular posible usando funciones (no se requieren módulos)
# 3) Documentar la tarea realizada sobre el propio código para facilitar el estudio posterior
#
#

from random import choice, sample


# En este diccionario se guardan las cartas y su puntuacion

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

#  F U N C I O N E S

def mostrarCartas():
    print(Fore.YELLOW)
    print (" Relacion de cartas y puntuaciones")
    print (" Ordenadas por puntuacion descendente")
    for key, value in sorted(cartas.items(), cartas.value(), reverse= True):
        print (value, key)
    
    print("Cartas: {}".format(" ".join(cartas.keys())))
    print("Puntos: {}".format(list(cartas.values())))



def avisarInicioPartida():
    # Preparativos antes de empezar la partida
    print(Fore.YELLOW)
    print()
    print(" Hola, soy el ordenador y vamos a jugar al blackjack (21)")
    print(" 1) El juagadpr escogera 2  cartas a su gusto")
    print(" 2) El ordenador escogera dos cartas al azar")
    print(" El que se aproxime mas a 21 sin pasarse gana!!!")
    print("---- EMPIEZA LA PARTIDA ----")

def avisarFinPartida():
    print(Fore.YELLOW + "---- LA PARTIDA HA FINALIZADO ---- ")
    print()

def jugar():
    print (" 3) Black Jack")
    lista_cartas= list(cartas)

    print(" Ha seleccionado:" end=" ")
    carta= choice(lista_cartas)
    score= cartas[carta]
    print(carta, end= "")
    carta= choice(lista_cartas)
    score += cartas[carta]
    print(carta, end= " ")
    print(" >>> su puntuacion es de", score)

    main_banca= sample(lista_cartas,2)
    score_banca= sum(cartas[carta] for carta in main_banca)
    print("La banca tiene: {} {} >> su score es {}".format(main_banca[0],
                                                            main_banca[1],
                                                            score_banca))

#
#
#  I N I C I O    P R O G R A M A
#
#
avisarInicioPartida()
mostrarCartas()
jugar()
avisarFinPartida()