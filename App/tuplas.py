#tuplas no se pueden modificar
from lib2to3.fixes.fix_tuple_params import tuple_name

t1: tuple[int, int, int] = (2, 3, 4)
t2 : tuple[int]  = (2,) #se grega la coma para identificar que es una tupla

x, y, z = t1 #Empaquetar las variables en la tupla

print(x)
print(y)
print(z)

x, y = y, x # Intercarmbiar los valores
