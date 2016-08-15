#Desdoblo los archivos de 1 hr en dos de 1/2 hr, y los grado como .csv
def desdoblar(ruta_entrada, ruta_salida, datos):

#Traigo las librerias que necesito
    import pandas as pd #traigo la libreria panda para estadistica
    import os
    import math as math

    for n in range(20, 23):
        datos_1mitad = pd.read_csv(ruta_entrada + datos + str(n) +'.dat', sep=',', header=None, nrows=35866,skiprows=4)
#abre tabla
#separaciones=',', sin header,toma la primer mitad de las filas,salta las primeras 4
        datos_1mitad.columns = ['time','record','u','v','w','Tsonica','coderr','voltaje'] #pongo header
#print(h11) #muestra en pantalla la tabla
        datos_1mitad.to_csv(ruta_salida + datos + str(n) +'_1.csv', index=None) #guardo el archivo de salida como .csv

        datos_2mitad = pd.read_csv(ruta_entrada + datos + str(n) +'.dat', sep=',', header=None, nrows=35866,skiprows=35866)
#abre tabla, salta la primer mitad de las filas
        datos_2mitad.columns= ['time','record','u','v','w','Tsonica','coderr','voltaje'] #pongo header
        datos_2mitad.to_csv(ruta_salida + datos + str(n) +'_2.csv', index=None)
    return
