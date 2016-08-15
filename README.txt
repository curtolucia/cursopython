La funcion 'main.py' es la principal, llama  a las demas

'desdoblar.py' Toma los datos en MIMO_2012 y parte los arvivos en dos (dos archivos de media hr de duracion) y los guarda como .csv
               Guarda los archivos en MIMO_2012_desdoblados

'valores_medios.py' Toma los valores desdoblados y calcula u, v, w, U y alfa medios
                    Los guarda en MIMO_2012_medios

'datos_totales.py' Toma los valores desdoblados y calcula U instantaneo
                   Guarda con el tiempo, u, v, w y U medio en MIMO_2012_totales

'desvios.py' Toma los valores totales y los medios de cada media hr y calcula u', v', w' y U_medio'
             Guarda con tiempo u', v', w' y U_medio' en MIMO_2012_flujos

'graf_cuad.py' Toma los valores de U_medio' y w' y grafica como scatter en los cuadrantes
               Grafica tambien la hiperbola 1/x en los 4 cuadrantes
               Guarda los graficos en MIMO_2012_cuad
