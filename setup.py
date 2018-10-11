from setuptools import find_packages, setup

from loamy.__version__ import __version__


def get_long_description():
    """Return the README."""
    return open("README.md", "r", encoding="utf8").read()


setup(
    name="loamy",
    version=__version__,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/erm/loamy",
    description="Something something something REST APIs...",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Jordan Eremieff",
    author_email="jordan@eremieff.com",
    entry_points={"console_scripts": ["loamy=loamy.cli:cli"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
