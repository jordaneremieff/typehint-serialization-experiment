from setuptools import find_packages, setup

from loamy.__version__ import __version__

setup(
    name="loamy",
    version=__version__,
    packages=find_packages(),
    license="MIT License",
    url="https://github.com/erm/loamy",
    description="Something something something REST APIs...",
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
)
