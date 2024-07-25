=============================
wrapture
=============================

.. image:: https://badge.fury.io/py/wrapture.png
    :target: http://badge.fury.io/py/wrapture

.. image:: https://travis-ci.org/mtllr/wrapture.png?branch=master
    :target: https://travis-ci.org/mtllr/wrapture

Transparently wrap multiple external API calls together and return standardized responses


Features
--------

* Create an extensible library using pluggy plugin infrastructure
* Add cross cutting concerns with configurable bridge patterns

Create Plugin
-------------

1. Make a setup.py file:
    ```python
    from setuptools import setup


    setup(
        name="wrapture-<myplugin>",
        install_requires="wrapture",
        entry_points={"wrapture": ["<myplugin> = lib"]},
        py_modules=["lib"],
    )
    ```
2. Make a lib.py file:
hook implementation details documented below
    ```python
    import wrapture

    @wrapture.hookimpl
    def hook1():
        ...

    @wrapture.hookimpl
    def hook2():
        ...
    ```

3. install the library so it is available on sys.path:
    `pip install wrapture-myplugin`
    or
    `pip install -e path/to/lib`

Plugin Hook implementation
--------------------------

Use the same structure for all hook implementations, but for the hookimpl wrapper, make sure you use the name implementation as needed in order to access the application api resources as necessary.

The plugin implementation is as follows
    ```python
    from typing import Any
    import wrapture

    @wrapture.hookimpl
    def run(cache,args, kwargs) -> Any:
        return cache(transform(call(*args, **kwargs)))

    def call(*args, **kwargs) -> Any:
        # return some data from your call
        ...

    def transform(data) -> Any:
        # return the data in the format that is needed for the application

    ```

NOTE: use the plugin as a simple plugin manager function call

Utils
-----

This is where the application cross cutting concerns are put: logging, caching, configuration.

The modules are named using the following convention: utils.<concern>.<libname>, eg: utils.cache.redis

Each concern has its own output type according to the concern type.

Logging does not output anything, caching outputs data or None...

Sync or async calls are managed in the utility library itself.


Configuration
-------------

TODO: configuration


Main.py
-------

Make a main.py module that integrates the plugins as needed


