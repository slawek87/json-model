# -*- coding: utf-8 -*-
from distutils.core import setup

try:
    with open('README.md', 'r') as f:
        readme = f.read()

    with open('LICENSE.txt', 'r') as f:
        license_ = f.read()
except:
    readme = ''
    license_ = ''

setup(
    name='json-model',
    version='1.0.1',
    packages=['json_model'],
    url='',
    download_url='https://github.com/slawek87/json-model',
    license=license_,
    author=u'Sławomir Kabik',
    author_email='slawek@redsoftware.pl',
    description='Json-Model is simple library to create Json Models from Python Objects. Library supports field validation by Python Types and required fields.',
    long_description=readme,
    keywords=['Python Json', 'Python serializers', 'Python Json Model'],
    install_requires=['setuptools'],
)
