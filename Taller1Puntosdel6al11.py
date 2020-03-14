#RESPUESTA PUNTOS DEL 6 AL 11 DEL TALLER #1 ARLEX SAAVEDRA COD:230171022

import re
import numpy as np

lectura = (open("E:\DonQuijote.txt",mode="r",encoding="utf-8")).read() #Realizamos la ubicacion del archivo para poderlo extraer
print(lectura)  #Se imprime el contenido del archivo .txt

print("-------------------------------")

cantidadLineas = re.findall("\n", lectura) #Con la función findall podemos saber donde ubieron saltos de linea
print("La cantidad de lineas son:", len(cantidadLineas)) # Imprimimos la cantidad de lineas con la funcion len ya que esta nos dara el numero exacto, ya que la funcion anterior solo arroja una lista

print("-------------------------------")

def word_count(str): #Aqui realizamos el conteo de cada una de las pabras del .txt
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print("Cantidad de veces que se repite cada palabra: \n") #Aqui imprimimos cada palabra del .txt y la cantidad de veces que se repite
for k, v in word_count(lectura).items():                         
    print("Palabra : {0}, Repeticion : {1}".format(k, v))

print("Palabras con mayor frecuencia, mayor a 2: \n") #Aqui imprimimos las palabras que se repiten mas de dos veces
for k, v in word_count(lectura).items():         
    if (word_count(lectura)[k] >= 3):  
        print("Palabra : {0}, Repeticion : {1}".format(k, v))

print("-------------------------------") #Aqui obenemos el conjunto de datos que mas se repiten con la libreria de numpy
x = np.array([]) 
y = np.array([])
#x = np.append(x, 1)
for k, v in word_count(lectura).items():         
    if (word_count(lectura)[k] >= 3):  
        x = np.append(x, k)
        y = np.append(y, v)

print(x) #imprimimos los parametros que quedan en el eje x, en este caso las palabras
print(y) #imprimimos los datos que quedan en el eje y, en este caso la frecuencia

print("Grafica:") #Procedemos a pasar los parametros de x e y para realizar su grafica
from matplotlib import pyplot as plt
plt.bar(x, y ,align = 'center')
plt.title('Frecuencia de palabras')
plt.ylabel('eje y')
plt.xlabel('eje x')
plt.show()