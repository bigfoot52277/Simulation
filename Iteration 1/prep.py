from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def primer():
    sand = biased_random(84, 228, 306, 67)
    mask = biased_random(168, 378, 744, 98)
    clean = biased_random(24, 126, 216, 47)
    mix = biased_random(288, 372, 504, 39)
    coat1 = biased_random(48, 84, 156, 17)
    flash = biased_random(600, 978, 1242, 176) 
    coat2 = biased_random(48, 84, 156, 17)
    dry = biased_random(2700, 3120, 3600, 195)
    cleanup = biased_random(126, 252, 408, 59)
    block = biased_random(78, 408, 1542, 187)
    primertime = sand+mask+clean+mix+coat1+flash+coat2+dry+cleanup+block
    return primertime

def prepare(Primer=False):
    movein = biased_random(12, 180, 336, 30)
    check = biased_random(30, 150, 600, 56)
    gather = biased_random(60, 90, 240, 28)
    sand = biased_random(360, 2898, 10800, 1180)
    brillo = biased_random(120, 456, 1800, 156)
    clean = biased_random(120, 276, 1200, 73)
    tape = biased_random(240, 3741, 14760, 1628)
    time_in = (movein+check+gather+sand+brillo+clean+tape)
    if Primer:
        primertime = primer()
        return (time_in+primertime)
    else:
        return time_in
