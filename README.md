[![image](https://img.shields.io/github/license/dksmiffs/devops-spt.svg)](https://github.com/dksmiffs/devops-spt)
[![image](https://img.shields.io/github/release/dksmiffs/devops-spt.svg)](https://github.com/dksmiffs/devops-spt/releases)
[![image](https://img.shields.io/travis/dksmiffs/devops-spt.svg)](https://travis-ci.org/dksmiffs/devops-spt)
[![image](https://img.shields.io/codecov/c/github/dksmiffs/devops-spt.svg)](https://codecov.io/gh/dksmiffs/devops-spt)
[![image](https://img.shields.io/codacy/grade/bfac5bbcdddd4e88b4e33381996bb2dc.svg)](https://app.codacy.com/project/dksmiffs/devops-spt/dashboard)

A Python package that automates useful devops tasks.

## Testing _devopts-spt_

_devops-spt_ can be tested from two different perspectives:

1.  **Unit tests**:  Development time, pre-publish tests. Run as follows from the top level directory in a clean venv:
```bash
python -m pip install -r requirements_travis_ci.txt
python -m pytest tests
```

2.  **Package tests**:  Post-publish tests, importing _devops-spt_ itself back from TestPyPI. Run as follows from inside the `tests` directory in a clean venv:
```bash
python -m pip install -r requirements_TestPyPI.txt
python -m pytest
```
