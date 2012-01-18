from problems.practice import squares as problem
from common.io import output

def main():
    problem_id =problem.__file__.split('/')[-1].split('.')[0] # Name of the file without '.py'
    output(problem_id, problem.fetcher, problem.solver)

if __name__ == '__main__':
    main()