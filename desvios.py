def desvios(ruta_entrada_totales, ruta_entrada_medios, ruta_salida, datos):
#Calculo de desvios (U')
    import pandas as pd

#leo los archivos de viento medio y viento instantaneo, y w medio e instantaneo
    for n in range(20, 23):
        for arch in range(1, 3):
            datos_totales=pd.read_csv(ruta_entrada_totales + datos + str(n) + '_' + str(arch) + \
            '.csv',header=0) #lee el archivo guardado
            datos_medios=pd.read_csv(ruta_entrada_medios + datos + str(n) + '_' + str(arch) + \
            '.csv',header=0)
#leo la fecha de la columna correspondiente del archivo fechayviento
            fechora = datos_totales['time']

#leo de los archivos las columnas correspondientes a U y Umedio
            viento_total = datos_totales['viento_total']
            viento_medio = datos_medios['viento_medio']
            viento_medio_matrix = viento_medio.as_matrix() #paso a matriz para restarlo

#leo de los archivos las columnas correspondientes a w y wmedio
            w = datos_totales['w']
            w_medio = datos_medios['w_medio']
            w_medio_matrix = w_medio.as_matrix() #paso a matriz para restarlo

#calculo U' y w'
            viento_desvio = viento_total - viento_medio_matrix
            w_desvio = w - w_medio_matrix

#calculo U'*w'
            flujo_uw = viento_desvio * w_desvio

#guardo fechora, u, v, U y w en un .csv
            resultados = (ruta_salida + datos + str(n) + '_' + str(arch) + '.csv')

            resultados_forma = "{dat1}, {dat2}, {dat3}, {dat4}\n"

                    #if not os.path.isfile(resultados):
            f = open(resultados, 'w') #abro arch resultados como escritura
            head = 'time,viento_desvio,w_desvio,flujo_uw\n' #encabezado
            f.write(head) #escribe el encabezado en el archivo
            f.close() #cierro archivo

            f = open(resultados, 'a') #abro de nuevo resultados pero como append
            dato = resultados_forma.format(dat1=fechora, dat2=viento_desvio, dat3=w_desvio, dat4=flujo_uw)
            #agrego datos abajo del encabezado
            f.write(dato)
            f.close()
