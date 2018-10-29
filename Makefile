
VERSION = 2.0.0

setup:
	pip install pipenv
	pipenv install --dev

clean:
	rm -r build/
	rm -r dist/

build:
	python setup.py sdist bdist_wheel

release:
	twine upload dist/*
