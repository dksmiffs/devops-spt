import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='devops_spt',
  version='0.0.2',
  author='Dave Smith',
  author_email='dave.k.smith@gmail.com',
  description='Devops support functions in a Python package',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/dksmiffs/devops_spt',
  packages=setuptools.find_packages(),
  install_requires=['requests'],
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
)

