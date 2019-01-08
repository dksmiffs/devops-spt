import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="devops_spt",
  version="0.0.1",
  author="Dave Smith",
  author_email="dave.k.smith@gmail.com",
  description="Devops support functions in a Python package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/dksmiffs/devops_spt",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)

