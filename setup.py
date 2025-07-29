from setuptools import setup, find_packages

setup(
    name='emotion-detector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ibm-watson',
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'emotion-detect=app.cli:main'
        ],
    },
)
