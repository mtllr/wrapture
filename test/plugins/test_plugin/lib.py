from typing import Any
import wrapture
import requests as rq

BASE_URL = "https://jsonplaceholder.typicode.com"

@wrapture.hookimpl
def call(*args, **kwargs) -> Any:
    """call the todos resource"""
    response = rq.get(BASE_URL+"/todos")
    return response.json()

@wrapture.hookimpl
def cast(data: Any) -> Any:
    return data
