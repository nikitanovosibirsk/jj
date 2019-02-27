from setuptools import setup, find_packages
import jj


setup(
    name="jj",
    version=jj.__version__,
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nikita Tsvetkov",
    author_email="nikitanovosibirsk@yandex.com",
    python_requires=">=3.6.0",
    url="https://github.com/nikitanovosibirsk/jj",
    license="Apache 2",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "aiohttp==3.5.4",
        "undecorated==0.3.0",
    ],
    tests_require=[
        "asynctest==0.12.2",
        "mypy==0.670",
        "flake8==3.7.7",
        "coverage==4.5.2",
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],
)
