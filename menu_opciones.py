from data_stark import*
from main import*
from os import system


while True:
    system("cls")
    opcion = (input(""" 
        \n A. Nombre de superheroes género masculino  
        \n B. Nombres de superheroes género femenino 
        \n C. Superheroe más alto de género masculino
        \n D. Superheroe más alta de género femenino 
        \n("E. Superheroe más bajo de género masculino: ")
        \n("F. Superheroe más baja del género femenino: ")
        \n("G. Promedio de altura de superheroes de género masculino: ")
        \n("H. Promedio de altura de superheroes de género femenino: ")
        \n("I. ")
        \n("J. Cantidad de superheroes con cada tipo de ojos")
        \n("K. Cantidad de superheroes con cada tipo de pelo")
        \n("L. Cantidad de superheroes que tienen cada tipo de inteligencia: ")
        \n("M.Listar todos los superhéroes agrupados por color de ojos.")
        \n("N. Listar todos los superhéroes agrupados por color de pelo. ")
        \n("O. Listar todos los superhéroes agrupados por tipo de inteligencia ")
        
        Ingrese la opción que desee: """ ))
    
    
    match opcion:
        case "A":
            nombres_masculino(lista_personajes)
        case "B":
            nombres_femenino(lista_personajes)
            
            
        case "C":
            superheroe_masculino_mas_alto(lista_personajes)
        case "D":
            superheroe_femenino_mas_alto(lista_personajes)
        case "E":
            superheroe_masculino_mas_bajo(lista_personajes)
            
        case "F":
            superheroe_femenino_mas_bajo(lista_personajes)
            
        case "G":
            promedio_superheroes_masculinos(lista_personajes)
            
        case "H":
            promedio_superheroes_femenino(lista_personajes)
        case "I":
            superheroe_masculino_mas_alto(lista_personajes)
            superheroe_femenino_mas_alto(lista_personajes)
            superheroe_masculino_mas_bajo(lista_personajes)
            superheroe_femenino_mas_bajo(lista_personajes)
        case "J":
            cantidad_superheroes_ojos(lista_personajes)
        case "K":
            cantidad_superheroes_pelo(lista_personajes)
        case "L":
            cantidad_inteligencia(lista_personajes)
        case "M":
            agrupacion_color_de_ojos()
        case "N":
            listar_superheroes_por_color_de_pelo()
        case "O":
            listar_superheroes_por_inteligencia()            
    system("pause")                


