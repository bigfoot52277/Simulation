from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def spray(): #Primer variable has not been impemented
    check = biased_random(30, 150, 600, 56) 
    code = biased_random(54, 84, 120, 14)  
    mix = biased_random(600, 720, 900, 56) 
    inspect_repair = biased_random(48, 72, 222, 11) 
    tack = biased_random(96, 186, 384, 42) 
    static = biased_random(78, 108, 126, 14) 
    gunprep = biased_random(6, 12, 18, 2) 
    midgunprep = biased_random(72, 84, 126, 6) 
    mix = biased_random(30, 48, 66, 8) 
    adhesion = biased_random(30, 48, 60, 8) 
    adflash = biased_random(180, 240, 300, 28) 
    sealer = biased_random(30, 98, 312, 32) 
    sealflash = biased_random(720, 840, 1080, 56) 
    base1 = biased_random(30, 72, 498, 20) 
    flash1 = biased_random(300, 360, 600, 28) 
    base2 = biased_random(30, 72, 498, 20) 
    flash2 = biased_random(300, 360, 600, 28) 
    base3 = biased_random(30, 72, 498, 20) 
    flash3= biased_random(300, 600, 900, 140) 
    mid1 = biased_random(30, 72, 498, 18) 
    flash4 = biased_random(300, 360, 600, 28) 
    mid2 = biased_random(30, 72, 498, 18) 
    flash5 = biased_random(480, 720, 900, 112) 
    clear1 = biased_random(30, 72, 498, 20) 
    flash6 = biased_random(480, 600, 900, 56) 
    clear2 = biased_random(30, 72, 498, 20) 
    bake = biased_random(2880, 3000, 3120, 56)
    return check+code+mix+inspect_repair+tack+static+gunprep+mix+base1+flash1+base2+flash2+base3+flash3+mid1+flash4+mid2+flash5+clear1+flash6+clear2+bake
