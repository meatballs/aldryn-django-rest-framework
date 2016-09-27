# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_django_rest_framework import __version__

setup(
    name='aldryn-django-rest-framework',
    version=__version__,
    description=open('README.rst').read(),
    author='Owen Campbell',
    author_email='owen.campbell@tanti.org.uk',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'Django>=1.7',
        'djangorestframework>=3.4',
        'aldryn-addons',
    ],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
)
