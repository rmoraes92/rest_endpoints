"""
The MIT License (MIT)

Copyright © 2024 Ramon Moraes <ramonmoraes.foss@gmail.com>

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

import unittest

from rest_endpoints import Endpoint
from rest_endpoints import Credential
from rest_endpoints import GET
from rest_endpoints import HttpMethodIsNotSupported


class EndpointTestCase(unittest.TestCase):

    def test_get_url(self):
        class FooEndpoint(Endpoint):
            domain = "http://foo"

        class FooBarEndpoint(FooEndpoint):
            path = "/bar"

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), "http://foo/bar")

    def test_get_url_appended_slash(self):
        class FooEndpoint(Endpoint):
            domain = "http://foo/"

        class FooBarEndpoint(FooEndpoint):
            path = "/bar"

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), "http://foo/bar")

    def test_get_url_missing_slash(self):
        class FooEndpoint(Endpoint):
            domain = "http://foo"

        class FooBarEndpoint(FooEndpoint):
            path = "bar"

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), "http://foo/bar")

    def test_get_url_variable(self):
        class FooEndpoint(Endpoint):
            domain = "http://foo"

        class FooBarEndpoint(FooEndpoint):
            path = "bar/{bar_id}"

        bar = FooBarEndpoint(bar_id=1)
        self.assertEqual(bar.get_url(), "http://foo/bar/1")

    def test_query_params_merging(self):
        class FooEndpoint(Endpoint):
            domain = "http://foo"
            query_params = {"hello": 1}

        class FooBarEndpoint(FooEndpoint):
            path = "bar"

            def get_query_params(self):
                return super().get_query_params(
                    {
                        "world": 2,
                    }
                )

        bar = FooBarEndpoint()
        self.assertDictEqual(bar.get_query_params(), {"hello": 1, "world": 2})

    def test_headers_merging(self):
        class FooEndpoint(Endpoint):
            domain = "http://foo"
            headers = {"hello": 1}

        class FooBarEndpoint(FooEndpoint):
            path = "bar"

            def get_headers(self):
                return super().get_headers(
                    {
                        "world": 2,
                    }
                )

        bar = FooBarEndpoint()
        self.assertDictEqual(bar.get_headers(), {"hello": 1, "world": 2})

    def test_unsupported_methods(self):
        class FooEndpoint(Endpoint):
            domain = "http://foo"

        class FooBarEndpoint(FooEndpoint):
            path = "bar"
            methods = [
                GET,
            ]

        c = Credential()
        with self.assertRaises(HttpMethodIsNotSupported):
            FooBarEndpoint(c).post()

    def test_credentials_headers(self):
        class TokenCredential(Credential):
            headers = {
                "Authorization": "Bearer FooBar",
            }

        class FooEndpoint(Endpoint):
            domain = "http://foo"
            headers = {
                "Content-Type": "application/json",
            }

        class FooBarEndpoint(FooEndpoint):
            path = "bar"

        c = TokenCredential()
        bar = FooBarEndpoint(c)
        headers = {
            "Authorization": "Bearer FooBar",
            "Content-Type": "application/json",
        }
        self.assertDictEqual(bar.get_headers(), headers)

    def test_credentials_query_params(self):
        class TokenCredential(Credential):
            query_params = {
                "token": "FooBar",
            }

        class FooEndpoint(Endpoint):
            domain = "http://foo"
            query_params = {
                "format": "json",
            }

        class FooBarEndpoint(FooEndpoint):
            path = "bar"

        c = TokenCredential()
        bar = FooBarEndpoint(c)
        query_params = {
            "token": "FooBar",
            "format": "json",
        }
        self.assertDictEqual(bar.get_query_params(), query_params)


if __name__ == "__main__":
    unittest.main()
