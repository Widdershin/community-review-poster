import os
from setuptools import setup
here = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    'praw',
    'requests',
    ]

test_requires = [
    'pytest',
    ]

setup(name='autoposter',
      install_requires=install_requires,
      tests_require=test_requires,
      version='0.1.0',
      author='Nick Johnstone',
      author_email='ncwjohnstone@gmail.com',
      packages=['autoposter', 'autoposter.test'],
      license='LICENSE',
      test_suite="py.test",
      )
