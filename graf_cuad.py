#Grafico de cuadrantes
def graf_cuad (ruta_entrada, ruta_salida, datos):

#Traigo las librerias que necesito
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

#Leo los archivos con los calculos
    for n in range(20, 23):
        for arch in range(1, 3):
            datos_desvios=pd.read_csv(ruta_entrada + datos + str(n) + '_' + str(arch) + \
            '.csv',header=0) #lee el archivo guardado
            fechora = datos_desvios.time
            viento_desvio = datos_desvios.viento_desvio
            w_desvio = datos_desvios.w_desvio

#Defino las hiperbolas
            x1=np.linspace(0.1,4,50)
            y1=1/(x1)

#Grafico las hiperbolas en los 4 cuadrantes
            plt.plot(x1,y1,'k')
            plt.plot(x1,-y1,'k')
            plt.plot(-x1,y1,'k')
            plt.plot(-x1,-y1,'k')

#Mantengo el grafico
            plt.hold(True)

#Grafico U' y w'
            plt.scatter(viento_desvio,w_desvio)
            plt.axis([-4, 4, -2, 2])

#Ejes centrados en el medio del grafico
            ax = plt.gca()  # gca stands for 'get current axis'
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.spines['bottom'].set_position(('data',0))
            ax.yaxis.set_ticks_position('left')
            ax.spines['left'].set_position(('data',0))

#Guardo el grafico con nombre 'cuad' adelante y formato .png
            plt.savefig('cuad' + '_' + ruta_salida + datos + str(n) + '_' + str(arch) + '.png',format='png')
    return
