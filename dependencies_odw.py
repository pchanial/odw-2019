import json
import subprocess

# retrieve all the top-level packages used by odw
cp = subprocess.run(
    ['pipreqs', 'python', '--print', '--no-pin'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    encoding='utf-8')

toplevel_dependencies = set(cp.stdout.splitlines())
toplevel_dependencies -= {'numpy', 'scipy'}
toplevel_dependencies = sorted(toplevel_dependencies)

# find all subdependencies
subdependencies = {}
for ipackage, package in enumerate(toplevel_dependencies, 1):
    print(f'Package {package} [{ipackage}/{len(toplevel_dependencies)}]:')
    cp = subprocess.run(
        f'johnnydep --output-format json {package}'.split(),
        stdout=subprocess.PIPE,
        encoding='utf-8')
    subdependencies[package] = set(_['name'] for _ in json.loads(cp.stdout))

# optional(?) dependency
subdependencies['bilby'].add('lalsuite')

all_dependencies = sorted(set().union(*subdependencies.values()))

with open('dependencies-odw.txt', 'w') as f:
    for package in all_dependencies:
        f.write(f'{package}\n')
