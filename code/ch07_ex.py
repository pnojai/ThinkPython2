import math

def mysqrt(a):
    epsilon = 1e-15
    x = a/2
    
    while True:
        #print(x)
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

print(100, mysqrt(100))
print(1000, mysqrt(1000))

def test_square_root():
    i = 1
    max_i = 10

    heading1 = 'a'+' '*3+'mysqrt(a)'+' '*5+'math.sqrt(a)'+' '*2+'diff'
    heading2 = '-'+' '*3+'---------'+' '*5+'------------'+' '*2+'----'

    print(heading1)
    print(heading2)
    
    while i < max_i:

        a = float(i)
        my_sq = mysqrt(a)
        math_sq = math.sqrt(a)
        diff = my_sq - math_sq
        print('{:0.1f} {:0.11f} {:0.11f} {:0.11}'.format(a, my_sq, math_sq, diff))

        i += 1

test_square_root()

def estimate_pi():
    '''
    The mathematician Srinivasa Ramanujan found an infinite series that can be used to
    generate a numerical approximation of 1 / π:

    1/π = 2√2/9801 *
                   ∞
                   ∑
                   k=0

                   of (4k)!(1103+26390k)/ (k!)^4 396^4k
    '''

    epsilon = 1e-15 # boundary for summation
    Q = 1 # initialize summation
    sig = 0 # sigma summation

    A = (2 * math.sqrt(2)) / 9801

    i = 0
    while Q > epsilon:
        N = math.factorial(4 * i) * (1103 + (26390 * i))
        D = math.factorial(i)**4 * 396**(4*i)
        
        # print(N)
        # print(D)

        Q = N/D
        # print(Q)

        sig += Q
        # print(sig)
        i += 1

    pi_recip = A * sig
    # print(pi_recip)

    return 1/pi_recip

print()

print(estimate_pi())
print(math.pi)
print(estimate_pi() - math.pi)
