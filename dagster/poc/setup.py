import setuptools

setuptools.setup(
    name="poc",
    packages=setuptools.find_packages(exclude=["poc_tests"]),
    install_requires=[
        "dagster==1.13.1",
        "dagit==0.15.2",
        "pytest",
    ],
)
