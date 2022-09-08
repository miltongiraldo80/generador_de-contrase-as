def conversor (tipo_pesos,valor_dolar):

    pesos = float (input(" ¿cuantos pesos"+ tipo_pesos + "tiene ?:"))
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str (dolares)
    print("tienes $ " + dolares + "dolares" ) 




menu = """
bienvenido al conversor de monedas

1 - pesos colombianos
2 - pesos mexicanos
3 - pesos argentinos

elige una opcion :  """

opcion = int(input( menu))

if opcion == 1 :
    conversor ("colombianos", 3875)
  
elif opcion == 2 :
    conversor ("mexicanos" , 64)

elif opcion == 3 :
    conversor ("argentinos" , 24)

else:
    print("ingresa una opcion correcta por favor")






#conversion pesos colombianos  a dolares
"""
pesos = float (input(" ¿cuantos pesos colombianos tiene ?:"))
valor_dolar = 4400
dolares = pesos / valor_dolar
dolares = round(dolares,2)
dolares = str (dolares)
print("tienes $ " + dolares + "dolares" )

# conversion dolares a pesos colombianos

dolares = float (input ("¿ cuantos dolares tienes ?:"))
valor_pesos = 0.00023
pesos = dolares / valor_pesos
pesos = round (pesos,2)
pesos = str (pesos)
print("tienes" + pesos + "pesos")   

"""