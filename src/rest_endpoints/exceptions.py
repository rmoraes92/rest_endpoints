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


class HttpMethodIsNotSupported(Exception):
    def __init__(self, method, methods):
        """
        Params:
            method (str):
                String representing the method that's not supported
            methods (list of str):
                List of Strings representing the supported methods
        """
        msg = f'"{method}" is not in the list of supported methods: {methods}'
        super().__init__(msg)


class CouldNotImportAioHttpModule(Exception):

    def __init__(self):
        super().__init__(
            "make sure you installed with "
            "pip install rest-endpoint[async]"
        )
