import sys

def get_problem_id():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return raw_input('Enter the problem id: ')

def import_problem(problem_id):
    try:
        return __import__('problems.%s' % problem_id, globals(), locals(), ['solver', 'fetcher'], -1)
    except ImportError:
        print 'Failed to import the module "%s". It\'s either missing or invalid' % problem_id
        sys.exit(1)
