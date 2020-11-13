#
# https://en.wikipedia.org/wiki/Ackermann_function
# Ackermann Function
#

def ack(m, n):
    
    if m == 0:
        return n + 1

    elif m > 0 and n == 0:
        return ack( m - 1, 1)

    elif m > 0 and n > 0:
        return ack( m - 1, ack(m, n -1 ))

print(ack(3, 4))

# print(ack(4, 5))
# RecursionError: maximum recursion depth exceeded in comparison

print(ack(-1, -4))

print(ack(0, -4))