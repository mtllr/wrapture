"""
utility to make a new plugin with setup.py entry points
"""

import os
from datetime import date

# TODO MOVE MAIN() IN OWN FILE: HOST.PY
LIB_PY = \
"""
# ### {plugin_name}  ###
# Copyright (C) {year} {author_name}.
#
# MIT Licence

import wrapture
from typing import Any

@wrapture.hookimpl
def run(args: list, kwargs: dict) -> Any:
    return transform(call(args, kwargs))

def call(args: list, kwargs: dict) -> Any:
    # implement how the data is called
    ...

def transform(data: Any) -> Any:
    # implement how the data schema is transformed
    ...
"""



def main():
    """
    make a new plugin for wrapture
    """
    author_name = input("author full name: ") or ""
    author_mail = input("author email: ") or ""
    plugin_name = input("plugin name: ") or ""
    year = date.today().year

    # Make the plugin directory in the plugins folder
    dest = f"wrapture/lib/{plugin_name}.py"
    os.makedirs(dest)

    # Make the setup.py file
    contents = {
        "author_name": author_name,
        "author_mail": author_mail,
        "plugin_name": plugin_name,
        "year": year
        }
    # ic(contents)
    lib_content = LIB_PY.format(**contents)
    with open(dest, "w") as fh:
        fh.write(lib_content)

    # Make the

if __name__=="__main__":
    main()