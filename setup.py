# setup.py

from setuptools import setup, find_packages

setup(
    name="protobase-client",
    version="0.1.0",
    description="A Python client for the ProtoBase authentication API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="AkiTheMemeGod",
    author_email="k.akashkumar@gmail.com",
    url="https://github.com/AkiTheMemeGod/ProtoBase",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
