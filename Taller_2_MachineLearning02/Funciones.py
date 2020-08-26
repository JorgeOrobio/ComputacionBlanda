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



#print('División en profundidad =\n', np.dsplit(c,3), '\n')