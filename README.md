# Maglev
*🚧 Work-in-progress &mdash; not suitable for production 🚧*
### Super simple, template-based Async/IO web framework
![](train.jpg)

### Install
If you haven't already, you should get `python` and `pipenv` (installation depends on operating system).
> Maglev *requires* Python 3.5 or above. Check your python version by typing `python3 -V`.

```
$ cd test-project
$ pipenv install maglev
```
You should see `Pipfile` & `Pipfile.lock`. Do not touch these files; they are internal files used by `pipenv` for dependency resolution.

### Usage
```
$ pipenv run maglev-serve
```

Maglev will read the `./pages` folder. Every file with the extension `.mako` is mapped to a url (e.g. `hello.mako` will become `/hello`). `index.mako` will be mapped to the root and `404.mako` will be mapped to the 404 page. Any page starting with `_` is ignored.

For additional help, type `maglev-serve -h`.

> Pages are written with the Mako templating language. Information is available on the [official website](http://www.makotemplates.org/).
