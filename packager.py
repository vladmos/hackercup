from common.utils import get_problem_id
from common.packaging import pack_problem

def main():
    problem_id = get_problem_id()
    pack_problem(problem_id)

if __name__ == '__main__':
    exit_code = main()
