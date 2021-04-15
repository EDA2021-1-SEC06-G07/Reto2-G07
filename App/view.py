"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist as alt
from DISClib.DataStructures import arraylist as slt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import model


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar los n videos con más vistas de un categoría y país específico")
    print('4- Encontrar el video con más días en tendencia de una categoria específica')
    print('5- Encontrar los n cideos con más like de un país y un tag específico')

catalog = None

"""
Menu principal
"""

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()



def loadData(catalog):
    """
    Carga los libros en el catalogo
    """
    return controller.loadData(catalog)

catalog = None
    
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog= controller.initCatalog()
        carga = loadData(catalog)
        print("Tiempo[ms]:", f"{carga[0]:.3f}", "||", 
               "Memoria[kB]:", f"{carga[1]:.3f}")
        print('videos cargados: '+ str(alt.size(catalog['videos'])))
        print('Categorias cargadas: '+ str(slt.size(catalog['idname_category'])))
        print('Paises Cargados: '+ str(mp.size(catalog['country'])))
    
    elif int(inputs[0]) == 2:
        category = str(input('Ingrese la categoria: '))
        country = str(input('Ingrese el país: '))
        size = int(input('Ingrese el cantidad de videos: '))
        print('Consultando la información solicitada...')
        print(controller.load_Req_1(catalog['category'],category,country,size))

    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:    
        category = str(input('Ingrese la categoria: '))
        print('Consultando la información solicitada...')
        print(controller.load_Req_3(catalog['category'],category))

    elif int(inputs[0]) == 5:
        country = str(input('Ingrese el país: '))
        tag = str(input('Ingrese el tag: '))
        size = int(input('Ingrese el cantidad de videos: '))
        print('Consultando la información solicitada...')
        print(controller.load_Req_4(catalog['country'],country,size,tag))
    else:
        sys.exit(0)
sys.exit(0)

