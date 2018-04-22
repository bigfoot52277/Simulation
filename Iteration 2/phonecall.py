from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def gen_call_length():  # generates telephone call lenghts
    return float(biased_random(0, 762, 2724, 333))

def gen_call_time(): # generates inbound telephone call times
    return biased_random(15, 128, 365, 53)
