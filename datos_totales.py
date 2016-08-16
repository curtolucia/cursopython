#Calculo de viento total (U=(u^2+v^2)^(1/2))
def datos_totales(ruta_entrada, ruta_salida, datos):

#Traigo las librerias que necesito
    import pandas as pd

    for n in range(20, 23):
        for arch in range(1, 3):
            datos_desdoblados = pd.read_csv(ruta_entrada + datos + str(n) + '_' + str(arch) + '.csv',header=0)
            fechora = datos_desdoblados['time']
            u = datos_desdoblados['u']
            v = datos_desdoblados['v']
            w = datos_desdoblados['w']
            viento_total=(datos_desdoblados['u']**2+datos_desdoblados['v']**2)**(1/2) #U=(u^2+v^2)^(1/2)

#guardo fechora, u, v, U y w en un .csv
            resultados = (ruta_salida + datos + str(n) + '_' + str(arch) + '.csv')

            resultados_forma = "{dat1}, {dat2}, {dat3}, {dat4}, {dat5}\n"

            f = open(resultados, 'w') #abro arch resultados como escritura
            head = 'time,u,v,w,viento_total\n' #encabezado
            f.write(head) #escribe el encabezado en el archivo
            f.close() #cierro archivo

            f = open(resultados, 'a') #abro de nuevo resultados pero como append
            dato = resultados_forma.format(dat1=fechora, dat2=u, dat3=v, dat4=w, dat5=viento_total,index=None)
            #agrego datos abajo del encabezado
            f.write(dato)
            f.close()

#otra forma de guardar, concatenando
#            resultados = pd.concat([fechora, u, v, w, viento_total], axis=1, keys=['time', 'u', 'v', 'w', 'viento_total'])
#            resultados.to_csv = (ruta_salida + datos + str(n) + '_' + str(arch) + '.csv')
#        return
