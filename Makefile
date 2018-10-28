
VERSION = 1.0.1

setup:
	pip install pipenv
	pipenv install --dev

clean:
	rm -r build/
	rm -r dist/

build:
	python setup.py sdist bdist bdist_wheel

release:
	twine upload \
		dist/maglev-$(VERSION)-py3-none-any.whl \
		dist/maglev-$(VERSION).tar.gz
