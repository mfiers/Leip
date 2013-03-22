#!/usr/bin/env python

from setuptools import setup

DESCRIPTION = """
Ultralightweight python CLI framework
"""









setup(name='Leip',
      version='0.0.2',
      description=DESCRIPTION,
      author='Mark Fiers',
      author_email='mark.fiers42@gmail.com',
      url='http://mfiers.github.com/Leip',
      packages=['Leip'],
      requires=[
        'Yaco (>=0.1.11)',
        ],
      package_dir = {'Leip': 'leip'},
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          ]

     )
