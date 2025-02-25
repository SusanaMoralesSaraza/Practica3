#Definir una lista

b: list[int] = list() #lista vacia



#FUNCION ITERABLE O RECORRER

b: list[str] = list("HOLA") #lo que se iterable puede ir dentro del parentesis

# for i in   es un iterble osea que se puede recorrer


a: list[int] = [2, 3, 4] #  Acceder elementos de la lista
print(a[1])
print(a[-1])

a.append(10)  #Modificar una lista
print(a)

a.insert(-3, 20)  #Modificar una lista
print(a)

for valor in a:  # Recorrer una lista
    print(valor)

i = 0

while i < len(a):  # Recorrer una lista
    print(a[i])


#Rebanado de listas
print(a[1:5]) # va iuna posicion mas alla si quiero hasta 4 pongo 5 osea una mas alla

print(a[-5:-1]) #para coger la rebanada de atras hacia delante

print(a[-3:]) #Omito el ultimo valor ya que este dice que va hasta el final de la lista

print(a[1::2]) # omito el segundo valor porque es hasta el final y el tercer elemento me determina el salto

print(a[::-1]) # Copia la lista al reves

#modificar con rebanado
a[::2] = [0, 0, 0] # debe ser del mismo tamaño y debes ser iterable para cambiar esos elementos en la lista
print(a)
a[:-3:] = [50, 40, 34, 0] #agrega elemenmtos a la lista
