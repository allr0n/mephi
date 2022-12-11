import math

def f(x):
    y = float()
    if x < 1:
        try:
            y = math.atan(5*(x**2)) + 2 + (1 / (2*x - 1))
        except ZeroDivisionError:
            y = 'None'

    elif 1 <= x <= 3:
        y = math.fabs((x/3)+1)

    elif x > 3:
        y = math.exp(x/100)

    return y


def g(x,y):
    r = (x + 1 )**2 + (y - 4)**2
    if 2 <= x <= 4 and -4 <= x <= 5 and 4**2 < r < 6**2:
        return True
    else: 
        return False


def h(a,b,c):
    # (bx + 5)((c**2)*(x**2)+2acx+(a**2-36)=0
    def d(a,c):
        d = (2*a*c)*(2*a*c) - 4*(c**2)*(a**2-36)
        return d

    if b != 0:
        if a != 0:
            if c != 0:
                if d(a,c) < 0:
                    result = 1
                elif d(a,c) > 0:
                    result = 3
                else:
                    result = 2
            else: # c = 0
                if a == 6:
                    result = "continuum"
                else:
                    result = 1
        else:     # a = 0
            if c != 0:
                result = 3
            else: # c = 0
                result = 0
    else: # b = 0
        if a != 0:
            if c != 0:
                if d(a,c) < 0:
                    result = 0
                elif d(a,c) > 0:
                    result = 2
                else:
                    result = 1
            else: # c = 0
                result = 0             
        else:     # a = 0
            if c != 0:
                result = 2
            else: # c = 0
                result = 0 

    return str(result)