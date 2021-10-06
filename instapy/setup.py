from setuptools import setup

setup(name='instapy',
      version='0.2',
      description='Instagram filters in python',
      url='https://github.uio.no/IN3110/IN3110-bjorndre/tree/master/assignment4/instapy',
      author='Bjørn Dreyer',
      author_email='bjorndre@uio.no',
      packages=['filters', 'bin'],
      scripts=['bin/instapy.py',],
      entry_points={
          'console_scripts': ['instapy=bin.instapy:main'],
      },
)