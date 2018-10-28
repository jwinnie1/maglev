setup:
	pip install pipenv
	pipenv install --dev

build:
	python setup.py sdist bdist bdist_wheel
