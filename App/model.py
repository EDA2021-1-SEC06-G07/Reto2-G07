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
from DISClib.Algorithms.Sorting import mergesort as mes 
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
    addCountry(catalog,video)

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
    
def addCountry(catalog, video):
    countries = catalog["country"]
    video_country = video["country"]
    exist = mp.contains(countries,video_country)
    if exist:
        entry = mp.get(countries,video_country)
        country = me.getValue(entry)
    else: 
        country = newCountry()
        mp.put(countries,video_country,country)
    lt.addLast(country,video)
    
    
def newCountry():
    return lt.newList('SINGLE_LINKED',cmpVideosByViews)
    
    
def newCategory(idnumber,idnamecmp):
    dic = {'id_category': '',
            'name_category': '',
            'videos': None}
    dic['id_category'] = idnumber
    dic['name_category'] = idnamecmp
    dic['videos'] = lt.newList('ARRAY_LIST', cmpVideosByViews)
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

def cmpVideosByViews(video1, video2):
    if int(video1['views']) > int(video2['views']):
        return True
    elif int(video1['views']) < int(video2['views']):
        return False
    else: 
        if int(video1['likes']) > int(video2['likes']):
            return True
        else:
            return False

def cmpVideosbyLikes(video1,video2):
    if int(video1['likes']) > int(video2['likes']):
        return True
    elif int(video1['likes']) < int(video2['likes']):
        return False
    else: 
        if int(video1['views']) > int(video2['views']):
            return True
        else:
            return False

def cmpVideosByFreq(video1,video2):
    if int(video1['freq']) > int(video2['freq']):
        return True
    elif int(video1['freq']) < int(video2['freq']):
        return False
    else: 
        if str(video1['id']) > str(video2['id']):
            return True
        else:
            return False

def cmpVideosbyId(video1,video2):
    if int(video1['video_id']) > int(video2['video_id']):
        return True
    elif int(video1['video_id']) < int(video2['video_id']):
        return False
    else: 
        return True

# Funciones de ordenamiento
def sortVideos(lst,cmpfunction):
    sub_list = lst
    sorted_list= mes.sort(sub_list,cmpfunction)
    return  sorted_list
#Funciones de requerimiento
'Requerimiento #1'
def filtrar_PaisCategoria(mapCategory,category,country,size):
    categoria = mp.get(mapCategory,category)
    valueCat = me.getValue(categoria)
    lst_videos = valueCat['videos']
    new_list = lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(lst_videos):
        if video['country']==country:
                alt.addLast(new_list,video)  
    sorted_list= sortVideos(new_list,cmpVideosByViews)  
    lst_n = lt.subList(sorted_list,1,size) 
    return lst_n

"Requerimiento #2"
def filtar_paisTendencia(mapCountry, country):
    pais= mp.get(mapCountry,country)
    lst_videos = me.getValue(pais)
    new_list =  lt.newList(datastructure= 'ARRAY_LIST')
    for video in lt.iterator(lst_videos):
        if video['country'] == country:
            lt.addLast(new_list,video)
    videosByFreq = añadir_frecuencia(new_list)
    videosSorted = sortVideos(videosByFreq,cmpVideosByFreq)
    video_rta = alt.firstElement(videosSorted)
    return filtrar_req2(video_rta)

'Requerimiento #3'
def video_mas_dias_tendencia(mapCategory,category):
    categoria = mp.get(mapCategory,category)
    valueCat = me.getValue(categoria)
    lst_videos = valueCat['videos']
    new_list = lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(lst_videos):
        if (video['video_id']!= '#NAME?'):
            lt.addLast(new_list,video)
    videosByFreq = añadir_frecuencia(new_list)
    videosSorted = sortVideos(videosByFreq,cmpVideosByFreq)
    video_rta = alt.firstElement(videosSorted)
    return filtrar_req3(video_rta)

def añadir_frecuencia(lst):
    new_list = lt.newList(datastructure='ARRAY_LIST')
    dic_list = lt.newList(datastructure='ARRAY_LIST')

    for video in lt.iterator(lst):
        if alt.isPresent(new_list,video['video_id']):
            for dic in lt.iterator(dic_list):
                if dic['id'] == video['video_id']:
                    dic['freq'] += 1  
        else: 
            dic={'id': video['video_id'],
                'freq': 1,
                'video': video}
            alt.addLast(dic_list,dic)
            alt.addLast(new_list,video['video_id'])  
    return dic_list

'Requerimiento #4'
def videos_mas_likes(mapCountry,country,size,tag):
    pais = mp.get(mapCountry,country)
    videos = me.getValue(pais)
    new_list = lt.newList(datastructure='ARRAY_LIST')
    for video in lt.iterator(videos):
        if tag in video['tags']:
            lt.addLast(new_list,video)
    srt_lst = sortVideos(new_list,cmpVideosbyLikes)
    return lt.subList(srt_lst,1,size)

#Función filtrar datos
"Req_2"
def filtrar_req2(elmt):
    video = elmt['video']
    info_video ={
                'video': video['title'],
                'canal': video['channel_title'],
                'pais': video['country'],
                'diasTendencia': elmt['freq']
            }
    return info_video
"Req_3"
def filtrar_req3(elmt):
    video = elmt['video']
    info_video ={
                'video': video['title'],
                'canal': video['channel_title'],
                'categoria': video['category_id'],
                'diasTendencia': elmt['freq']
            }
    return info_video
