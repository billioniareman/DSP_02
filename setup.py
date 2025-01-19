from setuptools import find_packages, setup
from typing import List

# Define the editable install identifier
HYPHEN_E = '-e .'

def get_requirements(path: str) -> List[str]:
    requirements = []
    try:
        with open(path, 'r') as f:
            requirements = f.readlines()
            # Strip newline characters and whitespace
            requirements = [req.strip() for req in requirements]
            # Remove '-e .' if present
            if HYPHEN_E in requirements:
                requirements.remove(HYPHEN_E)
    except FileNotFoundError:
        print(f"Requirements file not found: {path}")
    return requirements

# Setup function for the package
setup(
    name='DSP02',
    version='0.0.1',
    author='Ayush Patidar',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
