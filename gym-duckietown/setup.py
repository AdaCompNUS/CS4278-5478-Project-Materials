from setuptools import setup


def get_version(filename):
    import ast
    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError('No version found in %r.' % filename)
    if version is None:
        raise ValueError(filename)
    return version


version = get_version(filename='gym_duckietown/__init__.py')

with open('requirements.txt', 'r') as f:
    required_packages = [s.strip() for s in f.readlines()]

setup(
    name='gym_duckietown',
    version=version,
    keywords='duckietown, environment, agent, rl, openaigym, openai-gym, gym',
    packages=["gym_duckietown"],
    install_requires=required_packages,
    entry_points={
        'console_scripts': [
            'duckietown-start-gym=gym_duckietown.launcher:main',
        ],
    },
    py_modues=[]
)
