import setuptools

setuptools.setup(
    name="poc",
    packages=setuptools.find_packages(exclude=["poc_tests"]),
    install_requires=[
        "dagster==0.15.2",
        "dagit==0.15.2",
        "pytest",
    ],
)
