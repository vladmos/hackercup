from common.utils import get_problem_id, import_problem
from common.io import output

def main():
    problem_id = get_problem_id()
    problem = import_problem(problem_id)
    output(problem_id, problem.fetcher, problem.solver)

if __name__ == '__main__':
    exit_code = main()
