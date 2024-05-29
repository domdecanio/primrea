from setuptools import setup, find_packages

setup(name='test_package',
      version='0.1',
      description='Access to PRIMRE knowledge hub metadata and content.',
      author='Dominick DeCanio',
      author_email='dominick.c.decanio@pnnl.gov',
#      license='',
      packages=find_packages(),
      install_requires=['pandas'])