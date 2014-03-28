#!/usr/bin/env python

from setuptools import setup

setup(
    name='mezzanine-openshift',
    version='1.3',
    description='Mezzanine configured for deployment on OpenShift.',
    author='Wahid',
    author_email='mohammad.wahid@bitsinglass.com',
    url='http://bitsinglass.com/',
    install_requires=[
        'Django>=1.5.1',
        'mezzanine>=1.4.7',
        'django_compressor>=1.3'
    ],
)
