import six
from typing import (
    Callable,
    MutableMapping,
    TypeVar,
    NewType,
    Any,
    Literal,
    List,
    Dict
)

HTTP_METHODS = Literal['GET', 'POST', 'PUT', 'PATCH']

SUPPORTED_CURRENCIES = Literal['ZAR', 'NGN']

SUPPORTED_COUNTRIES = Literal['NG', 'GH', 'KE', 'UG', 'ZA', 'TZ']
