"""
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
"""

import json
import requests
from rest_endpoints.exceptions import HttpMethodIsNotSupported
from rest_endpoints.methods import (
    GET,
    POST,
    PUT,
    PATCH,
    DELETE,
)


class Endpoint(object):

    domain = None
    path = None
    headers = None
    query_params = None
    methods = []

    def __init__(self, credential=None, *args, **kwargs):
        self.credential = credential
        self.path_params = kwargs or {}

    def get_path(self):
        return self.path.format(**self.path_params)

    def get_url(self):
        path = self.get_path()
        if self.domain[-1] == '/' and path[0] == '/':
            domain = self.domain[:-1]
        elif self.domain[-1] != '/' and path[0] != '/':
            domain = self.domain + '/'
        else:
            domain = self.domain
        return f'{domain}{path}'

    def get_headers(self, extra=None):
        ret = {}
        if self.credential:
            ret.update(self.credential.get_headers())
        ret.update(self.headers or {})
        ret.update(extra or {})
        return ret

    def get_query_params(self, extra=None):
        ret = {}
        if self.credential:
            ret.update(self.credential.get_query_params())
        ret.update(self.query_params or {})
        ret.update(extra or {})
        return ret

    def request(self, method, headers=None, query_params=None, data=None,
                json_data=None):
        if self.methods and method not in self.methods:
            raise HttpMethodIsNotSupported(method, self.methods)

        headers = self.get_headers(headers)
        params = self.get_query_params(query_params)
        url = self.get_url()
        if not data and json_data:
            data = json.dumps(json_data)

        fn = getattr(requests, method)
        if data:
            resp = fn(url=url, headers=headers, params=params, data=data)
        else:
            resp = fn(url=url, headers=headers, params=params)

        return resp

    def get(self, headers=None, query_params=None, data=None, json_data=None):
        return self.request(GET, headers, query_params, data, json_data)

    def post(self, headers=None, query_params=None, data=None, json_data=None):
        return self.request(POST, headers, query_params, data, json_data)

    def put(self, headers=None, query_params=None, data=None, json_data=None):
        return self.request(PUT, headers, query_params, data, json_data)

    def patch(
            self, headers=None, query_params=None, data=None, json_data=None):
        return self.request(PATCH, headers, query_params, data, json_data)

    def delete(
            self, headers=None, query_params=None, data=None, json_data=None):
        return self.request(DELETE, headers, query_params, data, json_data)

