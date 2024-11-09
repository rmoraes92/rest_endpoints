'''
The MIT License (MIT)

Copyright © 2024 Ramon Moraes

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


from rest_endpoints.methods import (
    GET,
    POST,
    PUT,
    PATCH,
    DELETE,
)
from rest_endpoints.credentials import Credential
from rest_endpoints.api import Endpoint
from rest_endpoints.exceptions import HttpMethodIsNotSupported


__version__ = "0.1.0"
__author__ = "Ramon Moraes"
__author_email__ = "nocfg@proton.me"
__license__ = "MIT"
__app_name__ = "rest_endpoints"
__description__ = "ReST API Endpoint mapper"
__all__ = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "Credential",
    "Endpoint",
    "HttpMethodIsNotSupported",
]
