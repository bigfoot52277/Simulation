from random import gauss, randint


def biased_random(minimum, mean, maximum, stdev):
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def deliver(cash=False): 
    intent = biased_random(5, 15, 30, 5)
    gather = biased_random(10, 25, 60, 5)
    signature = biased_random(2, 5, 15, 2)
    explain = biased_random(10, 25, 75, 7)
    passoff = biased_random(3, 5, 15, 1)
    walkaround = biased_random(186, 336, 1095, 70)
    cashier = biased_random(312, 486, 750, 81)
    # cash - variable if the customer has to be walked to the cashier
    if cash:
        return intent+gather+signature+explain+passoff+walkaround+cashier
    else:
        return intent+gather+signature+explain+passoff+walkaround

