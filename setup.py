# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname
import sys
# Fool distutils to accept more than ASCII
reload(sys).setdefaultencoding('utf-8')

version = '0.2'

setup(name='PasteCall',
    version=version,
    description="Paste entry point caller",
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='paste call entry point entrypoint entry_point deploy console',
    author=u'Linas Juškevičius',
    author_email='linas@idiles.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.testapp']),
    include_package_data=True,
    namespace_packages=['paste', 'paste.call'],
    zip_safe=True,
    install_requires=[
        'PasteScript',
        'PasteDeploy',
    ],
    test_suite='nose.collector',
    tests_require=['nose>=0.11'],
    entry_points="""
    [paste.global_paster_command]
    call = paste.call.commands:CallEP
    """,
)
