import sys
print( sys.int_info )
print( sys.float_info )
a = 10 ** 3300
print(a.bit_length( ) )   #이진수 크기를 알수 있다

print( "max", sys.float_info.max )
print( "min", sys.float_info.min )

l = [1, 2, 3, 4]
alias = l
print ( alias is l )
print ( alias == l )

lc = l.copy( )
print(lc == l )
print(lc  is l )

ld = list ( l )
print( ld == l )
print( ld is l )

import copy
l = [1, 2, 3, 4]
ll = [ l, l ]
print( ll )

lc = copy.deepcopy(ll)
print( lc )
lc[0][0] = 999
print( id( l ), id( ll[0] ), id( ll[1] ) )
print(lc) 

print(divmod(10,3))

print( any ( [ ] ) )
print( any ( [1, 0, 0 ] ) )
print( all ( [ ] ) )
print( all ( [1, 2, 0 ] ) )

print(type(any))

print(type(sorted))
i = ['abc', 'bc', 'a']
s = sorted(i)
print(s)

import random

print(random.randrange(1,10))
