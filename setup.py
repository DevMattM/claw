from setuptools import setup

#bring in __version__ from sourcecode
#per https://stackoverflow.com/a/17626524
#and https://stackoverflow.com/a/2073599

with open('claw/version.py') as ver:
    exec(ver.read())

setup(name='claw',
      version=__version__,
      description='The Claw - Used to download remote files via SFTP',
      url='http://github.com/devmattm/claw',
      author='Matthew McConnell',
      author_email='devmattm@gmail.com',
      license='APACHE2',
      packages=['claw'],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'claw = claw.claw:main',
          ],
      },
      install_requires=[
          'docopt==0.6.2',
          'pyyaml==3.12',
          'pysftp==0.2.9',
      ],
      zip_safe=False)
