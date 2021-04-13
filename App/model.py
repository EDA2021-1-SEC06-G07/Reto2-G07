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
from DISClib.DataStructures import arraylist as alt
from DISClib.DataStructures import singlelinkedlist as slt
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'video': None,
                'idname_category': None,
                'category': None,
               }
    catalog['videos'] = lt.newList(datastructure= 'ARRAY_LIST',
                                   cmpfunction = cmpVideosByCategory)

    catalog['idname_category'] = lt.newList(datastructure='ARRAY_LIST')

    catalog['category'] = mp.newMap(numelements=190000,
                                    loadfactor=4.0,
                                    maptype= "CHAINING")

    catalog['country'] = mp.newMap(numelements=190000,
                                    loadfactor=4.0,
                                    maptype= 'CHAINING')
    return catalog


# Funciones para agregar informacion al catalogo
def addIdName_Category(catalog,category):
    alt.addLast(catalog['idname_category'], category)

def addVideoCategory(catalog, video):
    alt.addLast(catalog['videos'], video)
    addCategory(catalog,video)

def addCategory(catalog, video):
    categories = catalog["category"]
    idnumber = video["category_id"]
    idname_cat= catalog['idname_category']
    idnamecmp = getNameCategory(idnumber,idname_cat)
    exist = mp.contains(categories,idnamecmp)
    if exist:
            entry = mp.get(categories, idnamecmp)
            category_id = me.getValue(entry)
    else:
            category_id = newCategory(idnumber,idnamecmp)
            mp.put(categories, category_id['name_category'], category_id)
    lt.addLast(category_id['videos'], video)
    
    
def newCategory(idnumber,idnamecmp):
    dic = {'id_category': '',
            'name_category': '',
            'videos': None}
    dic['id_category'] = idnumber
    dic['name_category'] = idnamecmp
    dic['videos'] = lt.newList('SINGLE_LINKED', cmpVideosByViews)
    return dic


# Funciones de consulta
def getVideosByCategory(catalog,category_id):
    category_id = mp.get(catalog["category"], category_id)
    if category_id:
        return me.getValue(category_id)['videos']

def getNameCategory(idnumber,idname):
    name= ''
    for elmt in lt.iterator(idname):
        if elmt['id'] == idnumber:
            name= elmt['name']
    return name



# Funciones utilizadas para comparar elementos dentro de una lista
def cmpByCategory(id1,entry):
    identry = me.getKey(entry)
    if  int(id1) == int(identry):
        return 0
    elif int(id1) > int(identry):
        return 1
    else:
        return -1

def cmpVideosByCategory(video1,video2):
    if video1['category_id'] == video2['category_id']:
        return 0
    elif video1['category_id'] > video2['category_id']:
        return 1
    else:
        return -1

def cmpVideosByViews(video1,video2):
    if video1['views'] == video2['views']:
        return 0
    elif video1['views'] > video2['views']:
        return 1
    else:
        return -1

# Funciones de ordenamiento
