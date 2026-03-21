from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Remove -e .
            if line == HYPEN_E_DOT:
                continue

            requirements.append(line)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Om',
    author_email='aryanmallick87@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)