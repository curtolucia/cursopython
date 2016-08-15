#Calculo de valores medios de u, v, w, U y alfa
def valores_medios(ruta_entrada, ruta_salida, datos):

#Traigo las librerias que necesito
    import pandas as pd #traigo la libreria panda para estadistica
    import os
    import math as math

    for n in range(20, 23):
        for arch in range(1, 3):
            d1h0_1=pd.read_csv(ruta_entrada + datos + str(n) + '_' + str(arch) + \
            '.csv',header=0) #lee el archivo guardado
            u_medio=d1h0_1['u'].mean(axis=0) #calculo la media de u
            v_medio=d1h0_1['v'].mean(axis=0) #calculo la media de v
            w_medio=d1h0_1['w'].mean(axis=0) #calculo la media de w
            viento_medio=((u_medio)**2+(v_medio)**2)**(1/2) #calculo el viento medio
            alfa=math.atan2(u_medio,v_medio)

#guardo fechora, u, v, w, U y alfa medios en un .csv
            resultados = (ruta_salida + datos + str(n) + '_' + str(arch) + '.csv')


            resultados_forma = "{dat1}, {dat2}, {dat3}, {dat4}, {dat5}\n"

            f = open(resultados, 'w') #abro arch resultados como escritura
            head = 'u_medio,v_medio,w_medio,viento_medio,alfa\n' #encabezado
            f.write(head) #escribe el encabezado en el archivo
            f.close() #cierro archivo
        #else:
            f = open(resultados, 'a') #abro de nuevo resultados pero como append
            dato = resultados_forma.format(dat1=u_medio, dat2=v_medio, dat3=w_medio, dat4=viento_medio, dat5=alfa)
#agrego datos abajo del encabezado
            f.write(dato)
            f.close()
