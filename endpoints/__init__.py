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


from endpoints.credentials import Credential
from endpoints.methods import GET
from endpoints.methods import POST
from endpoints.methods import PUT
from endpoints.methods import PATCH
from endpoints.methods import DELETE
from endpoints.api import Endpoint
from endpoints.exceptions import HttpMethodIsNotSupported


__version__ = "0.3.1"
__author__ = "Ramon Moraes"
__author_email__ = "ramonmoraes8080@gmail.com"
__license__ = "GPLv3"
__app_name__ = "endpoints"
__description__ = "ReST API Endpoint Mapper"
