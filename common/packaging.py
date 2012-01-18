import zipfile
import os

README_STRING = '''Run the solver: python runner.py %s

The framework for Facebook Hackercup solvers: https://github.com/vladmos/hackercup/
'''

SYSTEM_FILES = (
    'common/__init__.py',
    'common/io.py',
    'common/utils.py',
    'runner.py',
    'readme.txt',
    'problems/__init__.py'
)

def pack_problem(problem_id):
    readme_file = open('readme.txt', 'w')
    readme_file.write(README_STRING % problem_id)
    readme_file.close()

    with zipfile.ZipFile('packages/%s.zip' % problem_id, 'w') as zip_file:
        zip_file.write('input/input_%s.txt' % problem_id)
        zip_file.write('output')
        zip_file.write('problems/%s.py' % problem_id.replace('.', '/'))

        package_delimeter_indices = []
        current_index = -1
        while True:
            current_index = problem_id.find('.', current_index + 1)
            if current_index == -1:
                break
            else:
                package_delimeter_indices.append(current_index)

        for index in package_delimeter_indices:
            file_name = 'problems/' + problem_id[:index].replace('.', '/') + '/__init__.py'
            zip_file.write(file_name)

        for system_file in SYSTEM_FILES:
            zip_file.write(system_file)

    os.remove('readme.txt')