# responsible for creating ml application as a package and even deploy in py py
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:#filepath is string,function will return list
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n" , "") for req in requirements] #removing /n due to readlines
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements        

setup(
    name='mlproject',
    version="0.0.1",
    author = "Aryan Khurana",
    author_email='aryankhurana1701@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
# -e .   -> automatically runs setup.py file