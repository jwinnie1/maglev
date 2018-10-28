# Maglev

[![Build Status](https://travis-ci.org/jwinnie/maglev.svg?branch=master)](https://travis-ci.org/jwinnie/maglev)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/maglev.svg)](https://pypi.org/project/maglev)


*🚧 Work-in-progress &mdash; not suitable for production 🚧*
### Super simple, template-based Async/IO web framework
![](https://github.com/jwinnie/maglev/blob/master/train.jpg)

### Install
If you haven't already, you should get `python` and `pipenv` (installation depends on operating system).
> Maglev *requires* Python 3.5 or above. Check your python version by typing `python3 -V`.

```
$ mkdir test-project
$ cd test-project
$ pipenv install maglev
```
You should see `Pipfile` & `Pipfile.lock`. Do not touch these files; they are internal files used by `pipenv` for dependency resolution.

### Usage
```
$ pipenv run maglev-serve
```

Maglev will read the `./pages` folder. Every file with the extension `.mako` is mapped to a url (e.g. `hello.mako` becomes `/hello` and `blog/hello.mako` becomes `/blog/hello`). `index.mako` maps to `/` (`index.mako` in a subdirectory maps to the name of the subdirectory, e.g. `blog/index.mako` maps to `/blog`) and `404.mako` maps to the 404 page. Any page starting with `_` is ignored.

For additional help, type `maglev-serve -h`.

> Pages are written with the Mako templating language. Information is available on the [official website](http://www.makotemplates.org/).
