# https://www.facebook.com/hackercup/problems.php?pid=193824447299680&round=144428782277390

from itertools import combinations

def get_gcd((a, b)):
    """
    Greatest common divisor
    """
    while b:
        a, b = b, a % b
    return a

def solver((racers, probabilities)):
    overtakes_required = racers - 1

    ratios = []
    for turn_index, probability_pair in enumerate(probabilities):
        success_in_overtaking = 1 - 1. / probability_pair[0]
        success_in_normal_turn = 1 - 1. / probability_pair[1]

        ratio = success_in_normal_turn / success_in_overtaking

        ratios.append((turn_index, ratio))

    ratios.sort(key=lambda (i, ratio): ratio)

    numerator = 1
    denominator = 1

    for ratio_index, ratio in enumerate(ratios):
        if ratio_index < overtakes_required:
            current_turn_probability = probabilities[ratio[0]][0]
        else:
            current_turn_probability = probabilities[ratio[0]][1]

        numerator *= (current_turn_probability - 1)
        denominator *= current_turn_probability

    gcd = get_gcd((numerator, denominator))

    return '%s/%s' % (numerator / gcd, denominator / gcd)

def fetcher(input_stream):
    line = input_stream.next()
    data = line.split()
    data = [int(i) for i in data]

    racers = data[0]
    turns = data[1]

    probabilities = []
    for i in xrange(turns):
        probabilities.append((data[2 * i + 2], data[2 * i + 3]))

    return racers, probabilities