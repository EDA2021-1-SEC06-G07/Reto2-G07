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
 """
import time
import tracemalloc
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    tracemalloc.start()
    delta_time = -1.0
    delta_memory = -1.0
    
    start_time= getTime()
    start_memory = getMemory()
    loadIdName_Category(catalog)
    loadVideos(catalog)
    
    
    stop_time = getTime()
    stop_memory = getMemory()
    tracemalloc.stop()
    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory

    
def getTime():
    return(float(time.perf_counter()*1000))
def getMemory():
    return tracemalloc.take_snapshot()

def deltaMemory(start_memory,stop_memory):
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0
    for stat in memory_diff:
        delta_memory = delta_memory + stat. size_diff
    delta_memory = delta_memory/1024.0
    return delta_memory


# Funciones para la carga de datos
def loadVideos(catalog):
   
    videosfile = cf.data_dir + 'Samples/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        
        model.addVideoCategory(catalog, video)

def loadIdName_Category(catalog):
    file = cf.data_dir + 'Samples/category-id.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8',errors='ignore'),delimiter='\t')
    for category in input_file:
        name = category['name']
        name_mod = name.strip()
        name_cat= name_mod.lower()
        sub_catalog = {
            'id': category['id'],
            'name': name_cat
        }
        model.addIdName_Category(catalog, sub_catalog)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def load_Req_1(mapCategory,category,country,size):
    return  model.filtrar_PaisCategoria(mapCategory,category,country,size)
def load_Req_3(mapCategory,category):
    tracemalloc.start()
    delta_time = -1.0
    delta_memory = -1.0
    
    start_time= getTime()
    start_memory = getMemory()
    a= model.video_mas_dias_tendencia(mapCategory,category)
    print(a)
    stop_time = getTime()
    stop_memory = getMemory()
    tracemalloc.stop()
    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory 
def load_Req_4(mapCountry,country,size,tag):
    return model.videos_mas_likes(mapCountry,country,size,tag)