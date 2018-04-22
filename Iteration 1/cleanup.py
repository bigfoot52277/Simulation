from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def port():
    move_in = biased_random(12,180,336,30)
    gather = biased_random(30, 45, 120, 14)
    wash = biased_random(1098, 1584, 2562, 226)
    vaccum = biased_random(408, 696, 1482, 134) 
    dry = biased_random(204, 402, 588, 92)
    wax = biased_random(384, 990, 2718, 282)
    move_out = biased_random(12,180,336,30)
    time = move_in+gather+wash+vaccum+dry+wax+move_out
    return time # time the porter spends cleaning a car 

