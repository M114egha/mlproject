from setuptools import find_packages,setup
from typing import List ##as the function returns a list

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:   ##accepts the filepath as str and
                                                    ##returns the list of strings
    requirements=[] #Initialize empty list to hold the requirements                                               
    with open(file_path) as file_obj:#Open the file specified by th file opath
        requirements = file_obj.readlines() #Read all the lines from the file into list
        requirements=[req.replace("\n",'')for req in requirements] # Replace occurrences of "/n" with a space in each line

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements        


setup(
name='mlproject',
version='0.0.1',
author='Meghna',
author_email='meghabhairi114@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt'),


)
