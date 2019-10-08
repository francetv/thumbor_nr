import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = 'Thumbor Newrelic'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="thumbor_nr",
    version="1.0.0",
    author="Bertrand THILL",
    description=("Thumbor nr - France.tv Release"),
    license="MIT",
    keywords="thumbor nr",
    url="https://github.com/francetv/thumbor_nr",
    packages=[
        'thumbor_nr',
        'thumbor_nr.metrics'
    ],
    long_description=long_description,
    classifiers=[
        'Development Status ::4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'thumbor>=6.7.0'
    ]
)