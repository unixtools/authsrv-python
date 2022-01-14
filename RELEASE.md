authsrv release process
=======================

Make sure keyring is installed. Then can use:

  keyring set https://upload.pypi.org/legacy/ your-username
  keyring set https://test.pypi.org/legacy/ your-username

Expects python to be python 3.x

  autopep8 --max-line-length=120 -i -r -a -a authsrv

  python -m pip install --user --upgrade twine setuptools
  
  rm -rf dist
  python setup.py clean build sdist bdist_wheel
  twine upload --repository-url https://test.pypi.org/legacy/ dist/*

