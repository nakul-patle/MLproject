# Helps in creating the machine learning model as package and deploying
from setuptools import find_packages, setup
from typing import List

E_DOT = '-e .'  # Love KDOT


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)

    return requirements


setup(name='MLproject',
      version='0.0.1',
      author='Nakul Patle',
      author_email='nakulpatle321@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
      )
