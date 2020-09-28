=========
exceptiom
=========

Make python exceptions fun.

Installation
============

Install exceptiom using pip.

`pip install exceptiom`

We are on [PyPi](https://pypi.org/project/exceptiom/)

Visit us on [Github](https://github.com/aqua-regia/exceptioms)

Usage
=====
Import Exceptiom

`from exceptiom import Exceptiom`

and then raise exceptiom like

```
try:
    5 / 0
except Exception:
    raise Exceptiom('Failed while performing division')
```

You can also make it as the base class for all your derived exception.

Instead of doing `class MyException(Exception)` you can write `class MyException(Exceptiom)` 

Contributon
===========

To add jokes, just add joke in exceptiom/jokes_en and raise a PR.

For any other features raise a PR



