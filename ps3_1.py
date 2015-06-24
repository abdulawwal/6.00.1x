def radiationExposure(start, stop, step):
    r = 0;
    t = start
    while t < stop:
        r = r + f(t) * step
        print t, r
        t = t + step
    return r

def f(x):
    import math
    return 400*math.e**(math.log(0.5)/3.66 * x)

radiationExposure(0, 4, 0.25)
