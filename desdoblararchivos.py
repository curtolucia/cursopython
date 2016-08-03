#Script para desdoblar los archivos.dat del anemometro sonico
#Queremos separar los datos, que son cada 1 hr, en datos cada media hr
#Archivos original de 1 hr con 20 datos por seg. (20*3600 datos)

import pandas as pd #traigo la libreria panda para estadistica

h11 = pd.read_csv('Tabla2_0520.dat', sep=',', header=None, nrows=35866,skiprows=4)
#abre tabla
#separaciones=',', sin header,toma la primer mitad de las filas,salta las primeras 4
h11.columns= ['time','record','u','v','w','Tsonica','coderr','voltaje'] #pongo header
#print(h11) #muestra en pantalla la tabla
h11.to_csv('dia1hora11.csv') #guardo el archivo de salida como .csv

h12 = pd.read_csv('Tabla2_0520.dat', sep=',', header=None, nrows=35866,skiprows=35866)
#abre tabla, salta la primer mitad de las filas
h12.columns= ['time','record','u','v','w','Tsonica','coderr','voltaje'] #pongo header
h12.to_csv('dia1hora12.csv')

d1h10=pd.read_csv('dia1hora11.csv',header=0) #lee el archivo guardado
umedio=d1h10['u'].mean(axis=0) #calculo la media de u
vmedio=d1h10['v'].mean(axis=0) #calculo la media de v
wmedio=d1h10['w'].mean(axis=0) #calculo la media de w
vientomedio=((umedio)**2+(vmedio)**2)**(1/2) #calculo el viento medio

print('umedio=',umedio,'vmedio=',vmedio,'wmedio=',wmedio,'vientomedio=',vientomedio)
#muestra la media de u, v y w
valoresmedios='{name}medio'
valoresmedios.format(name='u')
valoresmedios.format(name='v')
valoresmedios.format(name='w')
valoresmedios.format(name='viento')
