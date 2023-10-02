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


class HttpMethodIsNotSupported(Exception):
    def __init__(self, method, methods):
        '''
        Params:
            method (str):
                String representing the method that's not supported
            methods (list of str):
                List of Strings representing the supported methods
        '''
        msg = f'"{method}" is not in the list of supported methods: {methods}'
        super().__init__(msg)

