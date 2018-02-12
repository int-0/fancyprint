#!/usr/bin/env python
'''
Fancy Print setup module
'''

__version__ = '0.0.1'
__author__ = 'Tobias Diaz'
__email__ = 'tobias.deb@gmail.com'
__license__ = 'GPLv3'

from setuptools import setup

setup(
    name='Fancy Print',
    version=__version__,
    description='Dumb tools to print in console',
    url='https://github.com/int-0/fancyprint',
    author='Tobias Diaz',
    author_email='tobias.deb@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='terminal development',
    packages=['fancyprint'],
)
