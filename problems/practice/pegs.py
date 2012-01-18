from collections import defaultdict

def get_next_row(row_index, row, missed_pegs):
    next_row = [defaultdict(lambda: 0) for i in xrange(len(row))]
    for i in xrange(len(row)):
        if (i + row_index) % 2 == 0: # Probably a peg
            peg_index = (row_index + 1, (i + 1) / 2)
            if peg_index not in missed_pegs:
                next_row[i] = None
                
    for i in xrange(len(row)):
        if row[i] is not None:
            descendants = [] # Columns where a row can go from the column i
            if next_row[i] is not None:
                descendants = [i]
            else:
                if i > 0:
                    descendants.append(i - 1)
                if i < len(row) - 1:
                    descendants.append(i + 1)

            for descendant_index in descendants:
                for key, value in row[i].iteritems():
                    next_row[descendant_index][key] += value / len(descendants)

    return next_row

def solver((rows, columns, target_column, missed_pegs)):

    # Build the first row
    # None stands for a peg, a dict stands for a free cell:
    # Keys are input columns and values are probabilities of a ball goes through given cell starting from the
    # input column
    row = [None] * (columns * 2 - 3)
    for column_index in xrange(columns - 1):
        row[2 * column_index] = {column_index: 1.}

    # Build all the next rows one by one
    for row_index in xrange(rows - 1):
        row = get_next_row(row_index, row, missed_pegs)

    # Get the answer
    target_column_data = row[2 * target_column]
    best_input_column = max(target_column_data.items(), key=lambda (x, y): y)

    return '%d %.6f' % best_input_column

def fetcher(input_stream):
    line = input_stream.next()
    input_data = [int(number) for number in line.split()]
    missed_pegs = set()
    for i in xrange(input_data[3]):
        missed_pegs.add((input_data[4 + 2 * i], input_data[5 + 2 * i]))
    return input_data[0], input_data[1], input_data[2], missed_pegs
