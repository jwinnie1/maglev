setup:
	pip install pipenv
	pipenv install --dev

clean:
	rm -r build/
	rm -r dist/

build:
	python setup.py sdist bdist bdist_wheel
