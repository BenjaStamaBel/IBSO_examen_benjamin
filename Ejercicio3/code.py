import pandas as pd
import sys
import re

def validar_entrada(texto):
    if texto.isalpha():
        return True
    else:
        print("La entrada contiene números. Por favor, ingrese solo letras.")
        return False

def validar_sku(sku):
  patron = r'^SKU-\d{1,3}$'
  value = bool(re.match(patron, sku))
  if value ==True:
        return True
  else:
        print("La entrada no coincide con el formato valido para el SKU ('SKU-xxx' donde las x son números)")
        return False


df = pd.read_csv(r"C:\Users\Benja\Downloads\IBSO\Prueba_Promociones.csv")
df['Fecha']=pd.to_datetime(df['Fecha'])

start_date = input('Introduce la fecha de inicio en formato dd-mm-yyyy o deja el campo en blanco: ')
end_date = input('Introduce la fecha final en formato dd-mm-yyyy o deja el campo en blanco: ')


while True:
    category = input('Introduce la categoría (en mayusculas) o deje en blanco: ')
    if validar_entrada(category):
        break
    else:
        continue 

while True:
    use = input('Introduce el uso (en mayusculas) o deje en blanco: ')
    if validar_entrada(use):
        break
    else:
        continue 

while True:
    sku = input('Introduce el SKU: ')
    if validar_sku(sku):
        break
    else:
        continue 


percentage = float(input('Introduce el valor del porcentaje en decimales de 0 a 1: '))
initial_inventory = int(input('Introduce el valor el inventario inicial como numero entero: '))

df['Week']=[fecha.isocalendar().week for fecha in df.Fecha]

if start_date=='' and end_date=='':
    data=df.set_index('Fecha').sort_index()
    print('1')
elif start_date=='':
    end_date=pd.to_datetime(end_date,dayfirst=True)
    data=df.set_index('Fecha').sort_index().truncate(after=end_date)
    print('2')
elif end_date=='':
    start_date=pd.to_datetime(start_date,dayfirst=True)
    data=df.set_index('Fecha').sort_index().truncate(before=start_date)
    print('3')
else:
    if pd.to_datetime(start_date,dayfirst=True)<df['Fecha'].min() or pd.to_datetime(end_date,dayfirst=True)>df['Fecha'].max():
        print('El rango de fechas es incorrecto,intente de nuevo')
        sys.exit()
    else:
        data=df.set_index('Fecha').sort_index().truncate(before=pd.to_datetime(start_date,dayfirst=True),after=pd.to_datetime(end_date,dayfirst=True))

data = data[data['Modelo']!='real']

if use =='':
    if category=='':
        data['Piezas']=data['Piezas']*(1+percentage)
    else:
        data = data[data['Categoria']==category]
        data['Piezas']=data['Piezas']*(1+percentage)
else:
    data = data[data['Uso']==use]
    data['Piezas']=data['Piezas']*(1+percentage)

print('Consumo de inventario para el SKU: '+sku)
print(initial_inventory)
for i in len(data[data['SKU']==sku]['Piezas']):
    x=data[data['SKU']==sku]['Piezas'][i]
    date=data[data['SKU']=='SKU-10'].index.values[i]
    initial_inventory=initial_inventory-x
    print(initial_inventory)
    if initial_inventory<=0:
        print('El inventario se acabó el día '+str(date)[:10])
        sys.exit()

print('No se acabó el inventario')




    


