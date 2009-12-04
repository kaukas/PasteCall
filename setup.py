from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='PasteCall',
      version=version,
      description="Paste entry point caller",
      long_description=open('README.txt').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='paste call entry point entrypoint entry_point deploy console',
      author='Linas Juskevicius',
      author_email='linas@idiles.com',
      url='www.idiles.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
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
