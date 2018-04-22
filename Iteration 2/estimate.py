from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def write_estimate():
    gather = biased_random(45, 90, 120, 21) 
    picture = biased_random(0, 260, 492, 121)
    data_input = biased_random(37, 130, 398, 43)
    explain = biased_random(18, 69, 332, 24)
    time = gather+picture+data_input+explain
    return time

def tdestimate(): # will be implemented in second round as an improvement option
    gather = biased_random(45, 90, 120, 21) 
    picture = biased_random(0, 260, 492, 121)
    tear_down = biased_random(300, 1080, 1920, 363)
    data_input = biased_random(37, 130, 398, 43)
    explain = biased_random(18, 69, 332, 24)
    time = gather+picture+tear_down+data_input+explain
    return time

def bodytime():
    return biased_random(0, 12.6, 65.6, 6.39)

def body_scale(time):
    return (time / 12.6)

def painttime(body_time):
    if body_time < 7:
        paint_time = biased_random(0, 7.92, 22.7, 3.69)
    else:
        paint_time = body_time * biased_random(0.35, 0.63, 0.86, 0.13)
    return paint_time

def paintscale(time):
    return (time / 7.92)
    

def laborscost(body_time):
    return body_time * biased_random(.65, 1.02, 14, 0.17)*100
