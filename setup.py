from setuptools import setup, find_packages

setup(
    name="temperature-converter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "requests",
        "python-dotenv",
    ],
)