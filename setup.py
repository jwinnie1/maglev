
from setuptools import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

pipfile = Project(chdir=False).parsed_pipfile

setup(
    name="maglev",
    version="2.0.0",
    author="Jeremy Potter",
    author_email="pypi@stormdesign.us",
    description=("PHP-like Async/IO web framework"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="GNU",
    keywords="web framework mako async asyncio",
    url="https://github.com/jwinnie/Maglev",
    install_requires=convert_deps_to_pip(pipfile["packages"], r=False),
    packages=["server"],
    scripts=["maglev"]
)
