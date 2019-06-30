authsrv release process
=======================

Expects python to be python 3.x

  autopep8 --max-line-length=120 -i -r -a -a authsrv

  python -m pip install --user --upgrade twine setuptools
  
  rm -rf dist
  python setup.py clean build sdist bdist_wheel
  twine upload --repository-url https://test.pypi.org/legacy/ dist/*

