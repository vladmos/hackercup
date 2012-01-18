import sys

from common.io import output

def get_problem_id():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return raw_input('Enter the problem id: ')

def main():
    problem_id = get_problem_id()
    try:
        problem = __import__('problems.practice.%s' % problem_id, globals(), locals(), ['solver', 'fetcher'], -1)
    except ImportError:
        print 'Failed to import the module "%s". It\'s either missing or invalid' % problem_id
        return 1

    output(problem_id, problem.fetcher, problem.solver)
    return 0

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
