# https://www.facebook.com/hackercup/problems.php?round=144428782277390

from collections import defaultdict, deque

def get_neighbours((row, column), total_rows, total_columns):
    neighbours = []
    if row > 0:
        neighbours.append((row - 1, column))
    if column > 0:
        neighbours.append((row, column - 1))
    if row < total_rows - 1:
        neighbours.append((row + 1, column))
    if column < total_columns - 1:
        neighbours.append((row, column + 1))
    return neighbours

def get_field_cell(field, index):
    return field[index[0]][index[1]]
    
def solver((field, start, end, colors)):
    rows = len(field)
    columns = len(field[0])

    get_field_cell(field, start)[1] = 0
    queue = deque([(0, start)]) # Step count, cell
    colors_reached = set()

    while True:
        current_step, current_cell_index = queue.popleft()
        current_step += 1

        current_cell = get_field_cell(field, current_cell_index)[0]

        color_neighbours = []
        if current_cell in '123456789' and current_cell not in colors_reached:
            colors_reached.add(current_cell)
            color_neighbours = [index for index in colors[current_cell] if index != current_cell_index]

        neighbours = get_neighbours(current_cell_index, rows, columns)
        for neigbour in neighbours + color_neighbours:
            neighbour_cell_data = get_field_cell(field, neigbour)
            if neighbour_cell_data[0] == 'W':
                continue
            elif neighbour_cell_data[0] == 'E':
                return current_step
            elif neighbour_cell_data[1] > current_step:
                neighbour_cell_data[1] = current_step
                queue.append((current_step, neigbour))
    
def fetcher(input_stream):
    line = input_stream.next()
    rows, columns = line.split()
    rows, columns = int(rows), int(columns)

    field = []
    colors = defaultdict(list)
    start, end = None, None

    for i in xrange(rows):
        line = input_stream.next()
        row = []
        for j, cell in enumerate(line):
            row.append([cell, 1000000])
            if cell in '123456789':
                colors[cell].append((i, j))
            elif cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
        field.append(row)

    return field, start, end, colors