# https://www.facebook.com/hackercup/problems.php?pid=193824447299680&round=144428782277390

from itertools import combinations

def get_gcd((a, b)):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def solver((racers, turns, probabilities)):
    turns_required = racers - 1

    best_result = (0, 1)
    for turn_indices in combinations(xrange(turns), turns_required):
        numerator = 1
        denominator = 1

        for i in xrange(turns):
            if i in turn_indices:
                probability = probabilities[i][0]
            else:
                probability = probabilities[i][1]

            numerator *= (probability - 1)
            denominator *= probability

        if float(numerator) / denominator > float(best_result[0]) / best_result[1]:
            best_result = numerator, denominator

    gcd = get_gcd(best_result)

    return '%s/%s' % (best_result[0] / gcd, best_result[1] / gcd)

def fetcher(input_stream):
    line = input_stream.next()
    data = line.split()
    data = [int(i) for i in data]

    racers = data[0]
    turns = data[1]

    probabilities = []
    for i in xrange(turns):
        probabilities.append((data[2 * i + 2], data[2 * i + 3]))

    return racers, turns, probabilities