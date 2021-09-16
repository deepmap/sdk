""" Install script for the Deepmap SDK. """

from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'asn1crypto==0.24.0', 'astroid==2.2.5', 'certifi==2019.3.9',
    'cffi==1.12.3', 'chardet==3.0.4', 'cryptography==2.7', 'idna==2.8',
    'isort==4.3.20', 'lazy-object-proxy==1.4.1', 'mccabe==0.6.1',
    'pycparser==2.19', 'PyJWT==1.7.1', 'requests==2.22.0', 'six==1.12.0',
    'typed-ast==1.4.3', 'urllib3==1.25.4', 'wrapt==1.11.1'
]

setup(
    name='deepmap_sdk',
    version='1.0',
    description='The Deepmap API SDK',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System:: OS Independent'
    ],
    keywords='Deepmap',
    url='',
    author='Mason Tian',
    author_email='masontian@deepmap.ai',
    licence='',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
)
