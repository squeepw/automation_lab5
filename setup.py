from setuptools import setup, find_packages

setup(
    name="your_project",
    version="0.1",
    packages=find_packages(),
    py_modules=["calculator"],  # Explicitly include root-level modules
)