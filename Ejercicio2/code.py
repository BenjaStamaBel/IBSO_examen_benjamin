def valor_letras(cadena):
  suma = 0
  for letra in cadena:
    if letra.islower():
      suma += ord(letra) - 96 
    elif letra.isupper():
      print(f"Cambia la {letra.upper() if letra.isalpha() else 'entrada'} en la posición {cadena.index(letra) + 1} a minúscula.")
      return
    else:
      print(f"Cambia el numero en la posición {cadena.index(letra) + 1} por una letra minúscula.")
      return

  return suma

cadena = input("Ingrese una cadena de letras minúsculas: ")

resultado = valor_letras(cadena)
if resultado is not None:
  print(f"La suma de los valores de las letras es: {resultado}")
