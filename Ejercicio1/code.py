import pandas as pd
import numpy as np

datos_climaticos = {}

datos_climaticos['CDMX']=np.random.randint(15,35,7)

datos_climaticos['PUEBLA']=np.random.randint(15,35,7)

datos_climaticos['MONTERREY']=np.random.randint(15,35,7)

datos_climaticos['MERIDA']=np.random.randint(15,35,7)

datos_climaticos['VERACRUZ']=np.random.randint(15,35,7)

datos_climaticos['ENSENADA']=np.random.randint(15,35,7)

datos_climaticos['MAZATLAN']=np.random.randint(15,35,7)

datos_climaticos_DF = pd.DataFrame.from_dict(datos_climaticos,orient='index',columns=['Lun','Mar','Mier','Jue','Vie','Sab','Dom'])
datos_climaticos_DF.index.names = ['Ciudad']

print(datos_climaticos_DF)

datos_climaticos_DF['Mean temp'] = datos_climaticos_DF.mean(axis=1)

datos_climaticos_DF['Max temp'] = datos_climaticos_DF.max(axis=1)

datos_climaticos_DF['Min temp'] = datos_climaticos_DF.min(axis=1)

print(datos_climaticos_DF)

print('Ciudad con temperatura promedio más alta')
print(datos_climaticos_DF[datos_climaticos_DF['Mean temp']==datos_climaticos_DF['Mean temp'].max()])

print('Ciudad con temperatura promedio más baja')
print(datos_climaticos_DF[datos_climaticos_DF['Mean temp']==datos_climaticos_DF['Mean temp'].min()])






# print('Promedio de temperatura por ciudad')
# print(datos_climaticos_DF.mean(axis=1))

# print('Promedio de temperatura por ciudad')
# print(datos_climaticos_DF.mean(axis=1))