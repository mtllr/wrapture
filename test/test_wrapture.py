"""
Tests for `wrapture` module.
"""
import pytest
from wrapture import hookspecs
import requests as rq
import pluggy

@pytest.fixture
def BASE_URL():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def LOGLIB():
    ...


@pytest.fixture
def CACHELIB():
    ...

@pytest.fixture
def LIB1():
    ...

@pytest.fixture
def LIB2():
    ...

@pytest.fixture
def PLUGIN():
    ...

# class TestWrapture(object):

#     @classmethod
#     def setup_class(cls):
#         pass

#     def test_something(self):
#         pass

#     @classmethod
#     def teardown_class(cls):
#         pass

def test_1_api_call_in_core_lib():
    from . import lib

    def get_plugin_manager():
        pm = pluggy.PluginManager("wrapture")
        pm.add_hookspecs(hookspecs)
        pm.register(lib)
        return pm

    pm = get_plugin_manager()
    Todos =pm.hook.call()

    assert Todos is not None



def test_1_api_call_with_hooked_calls_chaining():
    from . import lib

    def get_plugin_manager():
        pm = pluggy.PluginManager("wrapture")
        pm.add_hookspecs(hookspecs)
        pm.register(lib)
        return pm

    pm = get_plugin_manager()

    # NOTE: the plugin manager registers the library name as "test.lib"

    assert pm

    # class Todos:
    #     def __init__(self, hook) -> None:
    #         self.hook = hook

    #     def run(self):
    #         return self.cast(self.call())

    #     def call(self):
    #         return self.hook.run()

    #     def cast(self, data):
    #         ...

    # pendings = Todos(pm.hook)

    # result = pendings.run()

    # assert Todos is not None

def test_1_api_call_with_setuppy_lib():

    # NOTE: pip install plugins/test_plugin before running this test

    def get_plugin_manager():
        pm = pluggy.PluginManager("wrapture")
        pm.add_hookspecs(hookspecs)
        pm.load_setuptools_entrypoints("wrapture")
        return pm

    pm = get_plugin_manager()

    # NOTE: the plugin manager registers the library name as "lib"

    assert pm

def test_2_api_calls_in_parallel():
    ...


def test_2_api_calls_and_1_logging_call():
    ...


def test_1_core_lib_and_setup_mecanism():
    ...