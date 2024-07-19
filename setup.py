# Build command in local : python setup.py sdist
from setuptools import setup, find_packages

setup(
    name='test_package',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)