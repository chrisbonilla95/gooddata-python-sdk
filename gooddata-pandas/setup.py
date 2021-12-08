from setuptools import find_packages, setup

REQUIRES = ["gooddata-sdk==0.2", "pandas"]


def _read_version():
    with open("VERSION", "rt") as version_file:
        return version_file.readline().strip()


setup(
    name="gooddata-pandas",
    description="GoodData.CN to pandas",
    version=_read_version(),
    author="GoodData",
    license="MIT",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Database",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
    keywords=[
        "gooddata",
        "pandas",
        "series",
        "data",
        "frame",
        "data_frame",
        "analytics",
        "headless",
        "business",
        "intelligence",
        "headless-bi",
        "cloud",
        "native",
        "semantic",
        "layer",
        "sql",
        "metrics",
    ],
)