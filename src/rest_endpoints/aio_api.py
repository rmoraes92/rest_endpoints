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

from rest_endpoints.exceptions import HttpMethodIsNotSupported, CouldNotImportAioHttpModule

try:
    import aiohttp
except ModuleNotFoundError:
    raise CouldNotImportAioHttpModule()


from rest_endpoints.methods import DELETE, GET, PATCH, POST, PUT

from .api import Endpoint


class AsyncEndpoint(Endpoint):

    async def get(self, headers=None, query_params=None, data=None, json_data=None):
        return await self.request(GET, headers, query_params, data, json_data)

    async def post(self, headers=None, query_params=None, data=None, json_data=None):
        return await self.request(POST, headers, query_params, data, json_data)

    async def put(self, headers=None, query_params=None, data=None, json_data=None):
        return await self.request(PUT, headers, query_params, data, json_data)

    async def patch(self, headers=None, query_params=None, data=None, json_data=None):
        return await self.request(PATCH, headers, query_params, data, json_data)

    async def delete(self, headers=None, query_params=None, data=None, json_data=None):
        return await self.request(DELETE, headers, query_params, data, json_data)

    async def request(
        self, method, headers=None, query_params=None, data=None, json_data=None
    ):
        if self.methods and method not in self.methods:
            raise HttpMethodIsNotSupported(method, self.methods)

        headers = self.get_headers(headers)
        params = self.get_query_params(query_params)
        url = self.get_url()
        if not data and json_data:
            data = json.dumps(json_data)

        async with aiohttp.ClientSession() as session:
            fn = getattr(session, method)
            if data:
                async with fn(
                    url=url, headers=headers, params=params, data=data
                ) as response:
                    return response
            else:
                async with fn(url=url, headers=headers, params=params) as response:
                    return response
