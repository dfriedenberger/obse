from setuptools import setup
from obse import __version__

setup(name='obse',
      version=__version__,
      description='Library for Ontology Based System Engineering.',
      url='https://github.com/dfriedenberger/obse.git',
      author='Dirk Friedenberger',
      author_email='projekte@frittenburger.de',
      license='GPLv3',
      packages=['obse'],
      install_requires=[],
      zip_safe=False)
