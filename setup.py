from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[  # Add the dependencies here or use requirements.txt
        'flask', 'requests',  # Example dependencies
    ],
)