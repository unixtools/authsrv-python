all: package

package:
	rm -rf dist
	python setup.py clean build sdist bdist_wheel

tidy:
	autopep8 --max-line-length=120 -i -r -a -a authsrv
	pylint authsrv

testupload:
	twine upload --repository testpypi dist/*

upload:
	echo twine upload dist/*

install:
	pip install -e .

clean:
	rm -rf dist build *.egg-info __pycache__
	python setup.py clean
