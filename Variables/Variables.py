Nombre = "Focalors"
print(Nombre)

a = 9
b = 2
c = a * b
print(c)

Arcont = "venti"
Arcont = "Raiden"    
Arcont = "Furina"
"""La variable siempre va a priorizar a la linea mas nueva
en este caso Arcont sera Furina """
print(Arcont)

b += 10
print(b) 
"""Si se pone el += dara como resultado que 
cambiara el valor de la variable 
en este b=2 + 10 lo cual dara 12
Este efecto se puede acumular indefinidamente como usar
otro tipo de operaciones como por ejemplo:"""

d = 5
d += 10
d -= 10
print(d)

"CONCATENACION"
"""Esto es unir strings"""

Saludo = "hola owo"
BienvenidaSara = "Sara " + Saludo + " Como estas?"
print(BienvenidaSara)
"""Como se puede observar para separar la oracion en la impresion 
se tiene que poner un espacion en los valores de la variable al final 
y al principio dependiendo de lo que se utilize"""

"""Para concatenar de una mejor manera tambien se puede usar la siguiente
forma, esto tambien sirve para convertir cual tipo de dato a texto"""
#f-strings
BienvenidaSara2 = f"Sara {Saludo} Como andas?"
print(BienvenidaSara2)

"""Para eliminar datos definidos podemos usar DEL"""

del a

"""Para buscar palabras en las variables se puede usar el sig codigo
el cual te dira si la palabra esta en la variable osea true y si no
esta dira false"""
print("Como" in BienvenidaSara)
print("estas" not in BienvenidaSara)

#El gato solo sirve para dejar comentarios