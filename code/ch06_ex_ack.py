def ack(m, n):
    '''
    The Ackermann function, A(m, n), is defined:

    A(m, n) = 
    ⎧ 
    ⎪               n+1	if  m = 0 
    ⎨        A(m−1, 1)	if  m > 0  and  n = 0 
    ⎪A(m−1, A(m, n−1))	if  m > 0  and  n > 0.
    ⎩

    '''

    '''
    if (isinstance(m, int) == False or isinstance(n, int) == False):
        print('Error: arguments must be >= 0.')
        return
    else:
        # Let's create some cool print statements for viewing the trace.
        # This blows up pretty fast.
        space_m = ' ' * (4 * m)
        space_n = ' ' * (4 * n)
        print (space_m, 'ack_m', m)
        print (space_n, 'ack_n', n)
    '''
    
    if (isinstance(m, int) == False or isinstance(n, int) == False):
        print('Error: arguments must be >= 0.')
        return
    elif m == 0:
        return n + 1
    elif (m > 0 and n == 0):
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

print('*' * 70)
print(ack(1, 2))
print('*' * 70)
print(ack(2, 2))

print('*' * 70)
print(ack(3, 4))

print('*' * 70)
print(ack(3, 4))

