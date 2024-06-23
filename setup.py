from setuptools import setup
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "Housing-Predictor"
VERSION = "0.0.1"
AUTHOR = "Pradeep"
DESCRIPTION = "This is my first Machine Learning project Pipeline"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirements
    mentioned in requirements.txt file.
    return: This function is going to return a list 
    which contains the names of libraries mentioned in requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = requirement_file.readlines()
        requirements = [requirement.strip() for requirement in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
        return requirements

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())
