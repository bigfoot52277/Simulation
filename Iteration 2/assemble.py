from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def Assemble(): # these are the steps taken to put a car back together
    move_in2 = biased_random(12, 180, 336, 30)
    check_paint = biased_random(12, 180, 336, 30)# these are times in seconds
    put_together = biased_random(12, 180, 336, 30)
    move_out = biased_random(12, 180, 336, 30)
    return move_in2+check_paint+put_together+move_out
