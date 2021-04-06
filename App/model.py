"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.DataStructures import arraylist as al
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'video': None,
               'category': None,
               }
    catalog['videos'] = lt.newList(datastructure= 'ARRAY_LIST',
                                   cmpfunction = cmpVideosByCategory)

    catalog['category'] = mp.newMap(numelements=20000,
                                    loadfactor=4.0,
                                    maptype= "CHAINING",
                                    comparefunction= cmpByCategory     
                                )
    return catalog
# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    al.addLast(catalog['videos'], video)
    mp.put(catalog['category'], video['category_id'], video)
  
# Funciones de consulta

def getVideosByCategory(catalog,category_id):
    category_id = mp.get(catalog["category"], category_id)
    if category_id:
        return me.getValue(category_id)['videos']
    
# Funciones utilizadas para comparar elementos dentro de una lista
def cmpByCategory(id1,entry):
    identry = me.getKey(entry)
    if  int(id1) == int(identry):
        return 0
    elif int(id1) > int(identry):
        return 1
    else:
        return -1

def cmpVideosByLikes(video1,video2):
    if (video1['likes']== video2['likes']):
        return 0
    elif vide1['likes'] > video2['likes']:
        return 1
    else:
        return -1
    
def cmpVideosByViews(video1,video2):
    if (video1['likes']== video2['likes']):
        return 0
    elif vide1['likes'] > video2['likes']:
        return 1
    else:
        return -1
    
def cmpVideosByCategory(video1,video2):
    if (video1['category_id']== video2['category_id']):
        return 0
    elif video1['category_id'] > video2['category_id']:
        return 1
    else:
        return -1
# Funciones de ordenamiento
