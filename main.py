from data_stark import*

#1
def nombres_masculino(lista_personajes) -> str:
    
    for heroe_masculino in lista_personajes:
        if heroe_masculino["genero"] == "M":
            genero = heroe_masculino["nombre"]
            print(f"Superheroes masculinos: {heroe_masculino['nombre']}")
    return heroe_masculino
    
#2
def nombres_femenino(lista_personajes) -> str:
    for heroe_femenino in lista_personajes:
        if heroe_femenino["genero"] == "F":
            genero = heroe_femenino["nombre"]
            print(f"Superheroes femeninos: {heroe_femenino['nombre']}")
    return heroe_femenino        
    
#3
def superheroe_masculino_mas_alto(lista_personajes):
    altura_maxima = 0
    altura_maxima = float (lista_personajes[0]['altura'])
    superheroe_m_mas_alto = ""
    
    for heroe_masculino_alto  in lista_personajes:
        altura_normal = float (heroe_masculino_alto['altura'])
        
        if heroe_masculino_alto["genero"] == "M":
            genero = heroe_masculino_alto["nombre"]
        
            if altura_normal > altura_maxima:
                altura_maxima = altura_normal
                superheroe_m_mas_alto = genero
                
    print(f"El superheroe {superheroe_m_mas_alto} es el más alto y mide {altura_maxima} cm")
    return heroe_masculino_alto
    

        
#4
def superheroe_femenino_mas_alto(lista_personajes):
    altura_maxima = 0
    altura_maxima = float(lista_personajes[0]['altura'])
    superheroe_f_mas_alto = ""
    genero = ""
    
    for heroe_femenino_alto in lista_personajes:
        altura_normal = float(heroe_femenino_alto['altura'])
        
        if heroe_femenino_alto["genero"] == "F":
            genero = heroe_femenino_alto["nombre"]
        
        if altura_normal > altura_maxima:
            altura_maxima = altura_normal
            superheroe_f_mas_alto = genero
            
    print(f"La superheroe {superheroe_f_mas_alto} es la más alta y mide {altura_maxima} cm")
    return heroe_femenino_alto

#5
def superheroe_masculino_mas_bajo(lista_personajes):
    altura_minima = 0
    altura_minima = float(lista_personajes[0]['altura'])  
    superheroe_m_mas_bajo = ""
    
    
    for heroe_m_mas_bajo in lista_personajes:
        altura_normal = float(heroe_m_mas_bajo['altura'])
        
        if heroe_m_mas_bajo["genero"] == "M":
            genero = heroe_m_mas_bajo["nombre"]
        
        if altura_normal < altura_minima:
            altura_minima = altura_normal
            superheroe_m_mas_bajo = genero
            
    print(f"El superheroe masculino más bajo es {superheroe_m_mas_bajo} y su altura minima es {altura_minima}")
    return heroe_m_mas_bajo
    
#6
def superheroe_femenino_mas_bajo(lista_personajes):
    altura_minima = 0
    altura_minima = float(lista_personajes[0]['altura'])
    superheroe_femenino_mas_bajo = lista_personajes[0]['nombre']
    
    for superheroe in lista_personajes:
        if superheroe["genero"] == "F":
            altura_normal = float(superheroe['altura'])
            
            if altura_normal < altura_minima:
                altura_minima = superheroe["altura"]
                superheroe_femenino_mas_bajo = superheroe['nombre']
                
    print(f"El superheroe femenino más bajo es: {superheroe_femenino_mas_bajo} y su altura es {altura_minima}")
    return superheroe
    
#7
def promedio_superheroes_masculinos(lista_personajes) -> float:
    cantidad_masculinos= 0
    altura_masculinos = 0
    
    for superheroe in lista_personajes:
        if superheroe["genero"] == "M":
            
            altura_masculinos += float(superheroe['altura'])
            cantidad_masculinos +=1
        
        
        
    promedio = altura_masculinos / cantidad_masculinos
    print(f"El promedio de alturas de superheroes masculinos es: {promedio}")
    return superheroe

#8
def promedio_superheroes_femenino(lista_personajes) -> float:
    cantidad_femeninos = 0
    altura_femeninos = 0
    
    for superheroe in lista_personajes:
        
        if superheroe["genero"] == "F":
            altura_femeninos += float(superheroe['altura'])
            cantidad_femeninos +=1
        
    promedio = altura_femeninos / cantidad_femeninos
    print(f"El promedio de alturas de superheroes femeninos es: {promedio}")
    return superheroe
    
#9
#10
def cantidad_superheroes_ojos(lista_personajes) -> int:
    contador_ojos = {}
    
    for superheroes in lista_personajes:
        color_de_ojos = superheroes["color_ojos"]
        
        if color_de_ojos in contador_ojos:
            contador_ojos[color_de_ojos] +=1
        else:
            contador_ojos[color_de_ojos] =1
                
    print(f"Cantidad de superheroes con cada tipo de color de ojos {contador_ojos}")
    return superheroes
#11
def cantidad_superheroes_pelo(lista_personajes) -> int:
    contador_tipo_pelo = {}
    
    for superheroes in lista_personajes:
        color_de_pelo = superheroes["color_pelo"]
        
        if color_de_pelo in contador_tipo_pelo:
            contador_tipo_pelo[color_de_pelo] +=1
        else:
            contador_tipo_pelo[color_de_pelo] =1
                
    print(f"Cantidad de superheroes con cada tipo de color de pelo {contador_tipo_pelo}")
    return superheroes
#12
def cantidad_inteligencia(lista_personajes) -> int:
    contador_inteligencia = {}
    
    for superheroes in lista_personajes:
        tipo_inteligencia = superheroes.get("inteligencia", "No tiene")
        
        # if not tipo_inteligencia:
        #     inteligencia = "No tiene"
        
        if tipo_inteligencia in contador_inteligencia:
            contador_inteligencia[tipo_inteligencia] +=1
        else:
            contador_inteligencia[tipo_inteligencia] =1
                
    print(f"Cantidad de superheroes con cada tipo de inteligencia {contador_inteligencia}")
    return contador_inteligencia     
#13
def agrupacion_color_de_ojos():
    personajes_por_color = {}

    for personaje in lista_personajes:
        color_de_ojos = personaje["color_ojos"]

        if color_de_ojos in personajes_por_color:
            personajes_por_color[color_de_ojos].append(personaje)

        else:
            personajes_por_color[color_de_ojos] = [personaje]

    for color, personajes in personajes_por_color.items():
        print(f"Superheroes con ojos de color {color}: \n")
        for nombre in personajes:
            print(nombre["nombre"])
#14
def listar_superheroes_por_color_de_pelo():
    superheroes_por_color_de_pelo = {}
    
    for superheroe in lista_personajes:
        color_pelo = superheroe["color_pelo"]
        
        if color_pelo in superheroes_por_color_de_pelo:
            superheroes_por_color_de_pelo[color_pelo].append(superheroe)
        else:
            superheroes_por_color_de_pelo[color_pelo] = [superheroe]
    
    for color_pelo, superhéroes in superheroes_por_color_de_pelo.items():
        print(f"Superhéroes con pelo de color {color_pelo}:")
        for superheroe in superhéroes:
            print(f" {superheroe['nombre']}")
        print()
            
#15
def listar_superheroes_por_inteligencia():
    superheroes_por_inteligencia = {}
    
    for superheroe in lista_personajes:
        tipo_inteligencia = superheroe["inteligencia"]
        
        if tipo_inteligencia in superheroes_por_inteligencia:
            superheroes_por_inteligencia[tipo_inteligencia].append(superheroe)
        else:
            superheroes_por_inteligencia[tipo_inteligencia] = [superheroe]

    for tipo_inteligencia, superhéroes in superheroes_por_inteligencia.items():
        print(f"Superhéroes con tipo de inteligencia {tipo_inteligencia}:")
        for superheroe in superhéroes:
            print(f" {superheroe['nombre']}")
        print()

