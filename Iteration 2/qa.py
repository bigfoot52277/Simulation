from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def check(): # qa check with kickback to tech rates of joe = 23.2%, eddie = 47.6%, scott = 33.4%
    return biased_random(78, 210, 444, 61)
