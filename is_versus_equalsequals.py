# is vs ==

a = [1, 2, 3]
b = a

print( a == b )  # output: true

print( a is b )  # output: true

c = list(a)

print( a == c )  # output: true

print( a is c )  # output: false

##
## == -> evaluates to true if both objects content are equal
##
## is -> evaluetes to true if both objects are identical
##
