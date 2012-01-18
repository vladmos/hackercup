def input_stream(input_file):
    while True:
        line = input_file.readline()
        if not line:
            return
        line = line.strip()
        if line:
            yield line

def input(input_file):
    tasks_count = int(input_file.readline().strip())
    return tasks_count, input_stream(input_file)

def output(id, fetcher, solver):
    with open('input/input_%s.txt' % id, 'r') as input_file:
        tasks_count, line_stream = input(input_file)
        with open('output/output_%s.txt' % id, 'w') as output_file:
            for i in xrange(tasks_count):
                input_data = fetcher(line_stream)
                answer = solver(input_data)
                output_file.write('Case #%s: %s\n' % (i + 1, answer))
