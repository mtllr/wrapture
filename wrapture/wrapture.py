"""
    _summary_

_extended_summary_
"""
import os
import shutil
import abc
from datetime import date
from typing import Any
# from icecream import ic

class ConnectionBase(metaclass=abc.ABCMeta):
    def __init__(self, credentials) -> None:
        self.credentials = credentials

    def connect(self):
        """
        return a callable that can interact with the API service
        """

class WrapperBase(metaclass=abc.ABCMeta):
    """
    WrapperBase is the base class for the wrapture plugin implementations.
    """

    def __init__(self, connection: ConnectionBase, resource: str, method: str):
        self.connection = connection
        self.verb = resource
        self.method = method

    def run(self, args, kwargs) -> Any:
        """
        call and cast the data
        """
        return self.cast(self.call(*args, **kwargs))

    def call(self, *args, **kwargs)->Any:
        """
        call the API service
        """

    def cast(self, data: Any):
        """
        Change the data to the required format for the application
        """



SETUP_PY = \
"""
# Copyright (C) {year} {author_name}.
#
# MIT Licence

from setuptools import find_packages
from setuptools import setup

setup(
    name='{plugin_name}',
    version='{plugin_version}',

    description='{plugin_description}',

    author='{author_name}',
    author_email='{author_mail}',

    url='http://opendev.org/openstack/stevedore',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.8',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['wrapture.plugins.{plugin_name}',
              ],

    packages=find_packages(),
    include_package_data=True,

    entry_points={{
        'wrapture.plugins': [
            'field = stevedore.example2.fields:FieldList',
        ],
    }},

    zip_safe=False,
)
"""



def main():
    """
    make a new plugin for wrapture
    """
    author_name = input("author full name: ") or ""
    author_mail = input("author email: ") or ""
    plugin_name = input("plugin name: ") or ""
    plugin_version = input("plugin version [0.1.0]: ") or "0.1.0"
    plugin_description = input("plugin description: ") or ""
    year = date.today().year

    # Make the plugin directory in the plugins folder
    dest = "wrapture/plugins/"+plugin_name
    os.makedirs(dest)

    # Make the setup.py file
    contents = {
        "author_name": author_name,
        "author_mail": author_mail,
        "plugin_name": plugin_name,
        "plugin_version": plugin_version,
        "plugin_description": plugin_description,
        "year": year
        }
    # ic(contents)
    setup_content = SETUP_PY.format(**contents)
    with open(dest+"/setup.py", "w") as fh:
        fh.write(setup_content)

    # Make the

if __name__=="__main__":
    main()