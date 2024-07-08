
# Copyright (C) 2024 martin.
#
# MIT Licence

from setuptools import find_packages
from setuptools import setup

setup(
    name='plugin_test_2',
    version='0.1.0',

    description='plug test 2',

    author='martin',
    author_email='martin_mail',

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

    provides=['wrapture.wrapture.plugins.plugin_test_2',
              ],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'wrapture.example.formatter': [
            'field = stevedore.example2.fields:FieldList',
        ],
    },

    zip_safe=False,
)
