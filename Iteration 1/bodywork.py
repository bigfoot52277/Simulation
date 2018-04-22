import partsorder
from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def repair(Parts=False): # returns a total time in the techs hands doing actual body work and parts replacement
    move_in = biased_random(12, 180, 336, 30)
    check_estimate = biased_random(30, 150, 600, 56)
    check_parts = biased_random(30, 150, 600, 56)
    body_work = biased_random(159, 775, 1968, 286)
    send_paint = biased_random(12, 180, 336, 30)
    #parts = partsorder.order(second_order=True)
    #if Parts:
    #    return parts
    #else:
    return move_in+check_estimate+check_parts+body_work+send_paint
