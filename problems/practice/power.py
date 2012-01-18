# https://www.facebook.com/hackercup/problems.php?pid=187006817978553&round=144428782277390
# The page contains wrong answers in the example section, therefore my answers won't match it.
# However the following algorithm might be also wrong, but its answers are more optimal.

def get_army(money, generator_cost, warrior_cost, generators=None, warriors=None):
    if generators is not None:
        generators_money = generators * generator_cost
        warriors_money = money - generators_money
        warriors = warriors_money / warrior_cost
    else: # Assuming that warriors is not None
        warriors_money = warriors * warrior_cost
        generators_money = money - warriors_money
        generators = generators_money / generator_cost

    return generators, warriors

def solver((generator_cost, warrior_cost, money)):
    possible_answers = []
    for available_money in xrange(money - max(generator_cost, warrior_cost), money + 1):
        optimal_generators_count = available_money / (2 * generator_cost)
        optimal_warriors_count = available_money / (2 * warrior_cost)
        possible_answers.append(get_army(available_money, generator_cost, warrior_cost, generators=optimal_generators_count))
        possible_answers.append(get_army(available_money, generator_cost, warrior_cost, warriors=optimal_warriors_count))

    answer = max(possible_answers, key=lambda (generators, warriors): (generators * warriors, warriors))
    return answer[0] * answer[1]

def fetcher(input_stream):
    line = input_stream.next()
    data = line.split()
    data = [int(i) for i in data]

    return tuple(data)
