from setuptools import find_packages, setup

setup(
    name='libexamplepy',
    packages=find_packages(),
    version='0.0.1',
    description='My First Library',
    long_description = open("README.md").read(),
    author='MyName',
    license='MIT'
)