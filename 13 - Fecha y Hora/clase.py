from datetime import datetime, timezone, timedelta
import time

# Segundos usando la libreria TIME
# Este es el famoso TIMESTAMP
segundos = time.time()

print(f'Segundos (desde EPOCH): {segundos}')
# Segundos (desde EPOCH): 1660339556.0410001

# Fecha y hora actuales usando la libreria DATETIME
ahora = datetime.now()

print(f'Fecha Formateada (DATETIME): {ahora}')
# Fecha Formateada (DATETIME): 2022-08-12 18:25:56.041000

# Fecha y hora actuales pero GMT usando DATETIME
ahoraGMT = datetime.utcnow()

print(f'Fecha y hora UTC formateados (DATETIME): {ahoraGMT}')
# Fecha y hora UTC formateados (DATETIME): 2022-08-12 21:38:52.773243

# Fecha y hora desde un TIMESTAMP, usando otra zona horaria
fecha_desde_timestamp = datetime.fromtimestamp(segundos, timezone(offset=-timedelta(hours=3)))

print(f'Fecha y hora convertidos desde un TIMESTAMP: {fecha_desde_timestamp}')
# Fecha y hora convertidos desde un TIMESTAMP: 2022-08-13 05:59:58.558975+08:00

# Fecha y hora desde un TIMESTAMP, usando UTC
fecha_desde_timestamp = datetime.fromtimestamp(segundos, timezone.utc)

print(f'Fecha y hora convertidos desde un TIMESTAMP: {fecha_desde_timestamp}')
# Fecha y hora convertidos desde un TIMESTAMP: 2022-08-12 22:00:54.922144+00:00

# Format de datetime para tener SOLO la fecha como queremos
solo_fecha = ahora.strftime('%d-%m-%Y')

print(solo_fecha)
# 12-08-2022

'''
EJEMPLOS
'''

# Fecha para un archivo de log

# Obtenemos la fecha y hora actual:
ahora = datetime.now()

# Extraemos la fecha para usar de nombre de archivo
nombre_archivo = ahora.strftime('%Y%m%d') + '.txt'

print(nombre_archivo)
# 20220812.txt


