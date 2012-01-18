# https://www.facebook.com/hackercup/problems.php?pid=112921602098268&round=4

import math

def is_square(number):
    return int(math.sqrt(number)) ** 2 == number

def solver(number):
    answer = 0
    for i in xrange(number):
        first_square = i ** 2
        if first_square > number / 2.:
            break
        if is_square(number - first_square):
            answer += 1

    return answer

def fetcher(input_stream):
    return int(input_stream.next())