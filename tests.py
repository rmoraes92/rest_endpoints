'''
endpoints
Copyright (C) 2023  Ramon Moraes

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import unittest
from endpoints import Endpoint
from endpoints import Credential
from endpoints import GET
from endpoints import HttpMethodIsNotSupported


class EndpointTestCase(unittest.TestCase):

    def test_get_url(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'

        class FooBarEndpoint(FooEndpoint):
            path = '/bar'

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), 'http://foo/bar')

    def test_get_url_appended_slash(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo/'

        class FooBarEndpoint(FooEndpoint):
            path = '/bar'

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), 'http://foo/bar')

    def test_get_url_missing_slash(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

        bar = FooBarEndpoint()
        self.assertEqual(bar.get_url(), 'http://foo/bar')

    def test_get_url_variable(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'

        class FooBarEndpoint(FooEndpoint):
            path = 'bar/{bar_id}'

        bar = FooBarEndpoint(bar_id=1)
        self.assertEqual(bar.get_url(), 'http://foo/bar/1')

    def test_query_params_merging(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            query_params = {'hello': 1}

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

            def get_query_params(self):
                return super().get_query_params({
                    'world': 2,
                    })

        bar = FooBarEndpoint()
        self.assertDictEqual(bar.get_query_params(), {'hello': 1, 'world': 2})

    def test_headers_merging(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            headers = {'hello': 1}

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

            def get_headers(self):
                return super().get_headers({
                    'world': 2,
                    })

        bar = FooBarEndpoint()
        self.assertDictEqual(bar.get_headers(), {'hello': 1, 'world': 2})

    def test_unsupported_methods(self):
        class FooEndpoint(Endpoint):
            domain = 'http://foo'

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'
            methods = [
                GET,
                ]

        c = Credential()
        with self.assertRaises(HttpMethodIsNotSupported):
            FooBarEndpoint(c).post()

    def test_credentials_headers(self):
        class TokenCredential(Credential):
            headers = {
                'Authorization': 'Bearer FooBar',
                }

        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            headers = {
                'Content-Type': 'application/json',
                }

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

        c = TokenCredential()
        bar = FooBarEndpoint(c)
        headers = {
            'Authorization': 'Bearer FooBar',
            'Content-Type': 'application/json',
            }
        self.assertDictEqual(bar.get_headers(), headers)

    def test_credentials_query_params(self):
        class TokenCredential(Credential):
            query_params = {
                'token': 'FooBar',
                }

        class FooEndpoint(Endpoint):
            domain = 'http://foo'
            query_params = {
                'format': 'json',
                }

        class FooBarEndpoint(FooEndpoint):
            path = 'bar'

        c = TokenCredential()
        bar = FooBarEndpoint(c)
        query_params = {
            'token': 'FooBar',
            'format': 'json',
            }
        self.assertDictEqual(bar.get_query_params(), query_params)
