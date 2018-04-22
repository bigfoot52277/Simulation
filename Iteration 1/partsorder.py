from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def order(second_order=False):
    if not second_order:
        # Short delay
        delay = biased_random(12240, 24480, 48960, 5692)
    else:
        #Long delay
        delay = biased_random(19394, 189780, 518400, 79230)
    return delay

def process_parts():
    determine = biased_random(126, 322, 484, 91)
    order = biased_random(132, 252, 318, 56)
    return determine+order
