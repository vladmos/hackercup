# https://www.facebook.com/hackercup/problems.php?pid=188558297823727&round=4

from itertools import permutations

def solver(words):
    # Not an optimal solution but takes just two short lines of python code :)
    new_words = [''.join(sequence) for sequence in permutations(words)]
    return min(new_words)

def fetcher(input_stream):
    line = input_stream.next()
    return line.split()[1:]