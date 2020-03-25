import yaml


def read_requirements(filename):
    with open(filename) as f:
        data = f.read().split('\n')
    environment = {}
    for requirement in data:
        requirement = requirement.strip()
        if requirement == '':
            continue
        package, version = requirement.split('==')
        environment[package] = version
    return environment


def read_conda_environment(filename):
    with open(filename) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)['dependencies']
    environment = {}
    for requirement in data:
        package, version, *_ = requirement.split('=')
        environment[package] = version
    return environment


def read_dependencies(filename):
    with open(filename) as f:
        data = f.read().split('\n')
    return [_ for _ in data if _ != '']


def write_colab_requirements(filename, env1, env2, packages):
    env1 = {k.lower(): v for k, v in env1.items()}
    with open(filename, 'w') as f:
        for package in packages:
            if package == 'setuptools':
                # setuptools is not installed on colab, but pkg_resources
                # (which should be provided by setuptools) is loaded.
                # Since it is unlikely that setuptools is required for running
                # the packages, so ignore it
                continue
            if package not in env1 and package not in env2:
                print(f'Package {package} is not in colab and not in igwn')
                continue
            if package in env1 and package in env2 and env1[package] != env2[package]:
                print(f'{package}: {env1[package]} (colab) != {env2[package]} (igwn)')
            if package in env1:
                continue
            f.write(f'{package}=={env2[package]}\n')


# colab environment
colab_environment = read_requirements('environment-colab-20200325.txt')  # 391
igwn_environment = read_conda_environment('igwn-py36-testing.yaml')  # 453
odw_dependencies = read_dependencies('dependencies-odw.txt')  # 60

write_colab_requirements('requirements-colab.txt', colab_environment, igwn_environment, odw_dependencies)
