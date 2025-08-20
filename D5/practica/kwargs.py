""" KWARGS 
        def nombre_función(**kwargs)  
        --> La palabra 'kwargs' es reemplazable por cualquier otra, lo importante es que vaya acompañada de **
        --> (**kwargs) es una diccionario
"""

# PRÁCTICA 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parámetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    return len(kwargs)

print(cantidad_atributos(continent="América", country="Peru", city="Piura", x=1, y=2, z=3))

#...........................................................................................
# PRÁCTICA 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):

    lista = []

    for clave in kwargs:
        lista.append(clave)
        
    return lista

print(lista_atributos(x=1, y=2, z=3, color="Azul", sabor="Dulce"))
    
#...........................................................................................
# PRÁCTICA 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:
# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}

def describir_persona(nombre, **kwargs):   # Se puede tener a *arg y **kwargs juntos
 
    print(f"Caracteristicas de {nombre}:")
    
    for clave, valor in kwargs.items():   # items() devuelve a clave y a valor en una tupla
        print (f"{clave}: {valor}")
      
describir_persona('Mabel',color_ojos="azules", color_pelo="rubio")