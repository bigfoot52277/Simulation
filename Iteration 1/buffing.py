from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def buff(): # the time spent buffing a paint job in the second run this will be handled by the porter and not the painter.
    move_in = biased_random(12,180,336,30)
    gather = biased_random(30, 45, 120, 14)
    hand_sand = biased_random(45, 954, 2076, 423)
    machine_sand = biased_random(15, 270, 576, 119)
    buff = biased_random(126, 372, 942, 114)
    wipe_off = biased_random(15, 36, 108, 10)
    move_out = biased_random(12,180,336,30)
    time = move_in+gather+hand_sand+machine_sand+buff+wipe_off+move_out
    return time
