import numpy as np

a = np.arange(9).reshape(3,3)
print('a =\n', a, '\n')

b = a*2
print('b =\n', b)

print('Apilamiento horizontal =\n', np.hstack((a,b)),"\n" )

print( 'Apilamiento horizontal con concatenate = \n',
np.concatenate((a,b), axis=1) )

print( 'Apilamiento vertical =\n', np.vstack((a,b)) )

print( 'Apilamiento vertical con concatenate =\n',
np.concatenate((a,b), axis=0) )


print( 'Apilamiento en profundidad =\n', np.dstack((a,b)) )

print( 'Apilamiento por columnas =\n',
np.column_stack((a,b)) )

print( 'Apilamiento por filas =\n',
np.row_stack((a,b)) )



print('Array con división horizontal, uso de split() =\n',
np.split(a, 3, axis=1))


print('Array con división vertical, uso de split() =\n',
np.split(a, 3, axis=0))


# Para ilustrar con un ejemplo, utilizaremos una matriz de rango tres
c = np.arange(27).reshape(3, 3, 3)
print(c, '\n')
# Se realiza la división
print('División en profundidad =\n', np.dsplit(c,3), '\n')

# El atributo ndim calcula el número de dimensiones
print('ndim: ', b.ndim)

# El atributo size calcula el número de elementos
print('size: ', b.size)

# El atributo itemsize obtiene el número de bytes por cada
# elemento en el array
print('itemsize: ', b.itemsize)

# El atributo nbytes calcula el número total de bytes del array

print(b, '\n')
print('nbytes: ', b.nbytes, '\n')
# Es equivalente a la siguiente operación
print('nbytes equivalente: ', b.size * b.itemsize)

# El atributo T tiene el mismo efecto que la transpuesta de la matriz

b.resize(6,4)
print(b, '\n')
print('Transpuesta: ', b.T)

# Los números complejos en numpy se representan con j

b = np.array([1.j + 1, 2.j + 3])
print('Complejo: \n', b)

# El atributo real nos da la parte real del array,
# o el array en sí mismo si solo contiene números reales
print('real: ', b.real, '\n')
# El atributo imag contiene la parte imaginaria del array
print('imaginario: ', b.imag)

# Si el array contiene números complejos, entonces el tipo de datos

# se convierte automáticamente a complejo
print(b.dtype)

b = np.arange(4).reshape(2,2)
print(b, '\n')
f = b.flat
print(f, '\n')
# Ciclo que itera a lo largo de f
for item in f: print (item)
# Selección de un elemento
print('\n')
print('Elemento 2: ', b.flat[2])
# Operaciones directas con flat
b.flat = 7
print(b, '\n')
b.flat[[1,3]] = 1
print(b, '\n')
