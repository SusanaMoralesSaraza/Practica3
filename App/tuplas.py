#tuplas no se pueden modificar
from lib2to3.fixes.fix_tuple_params import tuple_name

t: tuple[int, int, int] = (2, 3, 4)
t2 : tuple[int]  = (2,) #se grega la coma para identificar que es una tupla

