from setuptools import setup,find_packages
from  typing import List
def get_file(file:str)->List[str]:
    requirements=[]
    hyphen_dot_e="-e ."
    with open(file) as file_obj:
        reqirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphen_dot_e in requirements:
            reqirements.remove(hyphen_dot_e)
    return reqirements
setup(
    name="ml_formal_project",
    version="0.0.1",
    author="Manas Agarwal",
    author_email="manasagarwal12921@gmail.com",
    packages=find_packages(),
    install_requires=get_file("requirements.txt")
)