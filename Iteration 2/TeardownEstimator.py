from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def tdestimate(): # will be implemented in second round as an improvement option
    gather = biased_random(45, 90, 120, 21) 
    picture = biased_random(0, 260, 492, 121)
    tear_down = biased_random(300, 2100, 9360, 837)
    data_input = biased_random(37, 130, 398, 43)
    explain = biased_random(18, 69, 332, 24)
    time = gather+picture+tear_down+data_input+explain
    return time
