[![image](https://img.shields.io/codacy/grade/bfac5bbcdddd4e88b4e33381996bb2dc.svg)](https://app.codacy.com/project/dksmiffs/devops-spt/dashboard)

A Python package that automates useful devops tasks.

## Testing _devopts-spt_

_devops-spt_ contains two types of tests, both contained under the top level `tests` directory:

1. **Unit tests**: Development time, pre-publish tests.  Use `requirements_travis_ci.txt` to populate a clean venv.  Then run as follows from the top level directory:
```bash
python -m pytest tests/local
```

2. **Package tests**: Post-publish tests, importing _devops-spt_ itself back from TestPyPI. Run as follows from the `tests/TestPyPI` directory in a clean venv:
```bash
python -m pip install -r requirements_TestPyPI.txt
python -m pytest
```
