ruta_entrada = './MIMO_2012/'
ruta_salida = './MIMO_2012_desdoblados/'
datos = 'Tabla2_05'

from desdoblar import desdoblar

desdoblar(ruta_entrada, ruta_salida, datos)

ruta_entrada = './MIMO_2012_desdoblados/'
datos = 'Tabla2_05'
ruta_salida = './MIMO_2012_medios/'

from valores_medios import valores_medios

valores_medios(ruta_entrada, ruta_salida, datos)

ruta_entrada = './MIMO_2012_desdoblados/'
ruta_salida = './MIMO_2012_totales/'
datos = 'Tabla2_05'

from datos_totales import datos_totales

datos_totales (ruta_entrada, ruta_salida, datos)

ruta_entrada_totales = './MIMO_2012_totales/'
ruta_entrada_medios = './MIMO_2012_medios/'
ruta_salida = './MIMO_2012_flujos/'
datos = 'Tabla2_05'

from desvios import desvios

desvios (ruta_entrada_totales, ruta_entrada_medios, ruta_salida, datos)

ruta_entrada = './MIMO_2012_flujos/'
ruta_salida = './MIMO_2012_cuad/'
datos = 'Tabla2_05'

from graf_cuad import graf_cuad

graf_cuad (ruta_entrada, ruta_salida, datos)
