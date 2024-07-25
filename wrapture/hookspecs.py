"""
    _summary_

_extended_summary_
"""
from datetime import date
from typing import Any, Union

import pluggy

hookspec = pluggy.HookspecMarker("wrapture")


@hookspec
def run(args: Union[list, tuple], kwargs: dict) -> Any:
    """
    successively run call then transform on the data acquired from the APIs

    :param args: required arguments for the API call
    :type args: list or tuple
    :param kwargs: extra keyword arguments for the call function
    :type kwargs: dict
    :return: any data returned from the API call, usually JSON
    :rtype: Any
    """
    return transform(call(args=args, kwargs=kwargs))

def call(args, kwargs) -> Any:
    """
    call the API service with arbitrary arguments and keyword arguments

    returns arbitrary data back
    """

def transform(data: Any) -> Any:
    """
    Change the data to the required format for the application

    returns arbitrary data
    """
