# rest-endpoints

A object oriented library that helps you map and organize your HTTP ReST API endpoint calls.


## Install

`pip install rest-endpoints`


## Usage

### Lets Map Urban Dictionary API

First step is creating a class responsible to handle how the credentials need
to injected on the HTTP requests

```python
from rest_endpoints import Credential


class ApiKeyCredential(Credential):
    headers = {
        "x-rapidapi-host": "mashape-community-urban-dictionary.p.rapidapi.com",
        "x-rapidapi-key": "SIGN-UP-FOR-KEY",
        "useQueryString": "true",
        }
```

Now lets map the class that will hold the shared domain and other data
(headers and query params) shared between endpoints

```python
from rest_endpoints import Endpoint


class CommunityUrbanDict(Endpoint):
    domain = "https://mashape-community-urban-dictionary.p.rapidapi.com"


class DefineEndpoint(CommunityUrbanDict):
    path = "/define"
```

For the sake of simplicity we will put all this together:


```python
from rest_endpoints import Credential
from rest_endpoints import Endpoint


class ApiKeyCredential(Credential):
    headers = {
        "x-rapidapi-host": "mashape-community-urban-dictionary.p.rapidapi.com",
        "x-rapidapi-key": "SIGN-UP-FOR-KEY",
        "useQueryString": "true",
        }


class CommunityUrbanDict(Endpoint):
    domain = "https://mashape-community-urban-dictionary.p.rapidapi.com"


class DefineEndpoint(CommunityUrbanDict):
    path = "/define"
```

Now we are going to use it to find the definition of _"wat"_:

```python
cred = ApiKeyCredential()
endpoint = DefineEndpoint(cred)
resp = endpoint.get(query_params={
    "term": "wat",
})

# resp here is a Response object from requests module/library
print(resp.status_code)
print(resp.content)
```

Wrapping it all up

```python
from rest_endpoints import Credential
from rest_endpoints import Endpoint


class ApiKeyCredential(Credential):
    headers = {
        "x-rapidapi-host": "mashape-community-urban-dictionary.p.rapidapi.com",
        "x-rapidapi-key": "SIGN-UP-FOR-KEY",
        "useQueryString": "true",
        }


class CommunityUrbanDict(Endpoint):
    domain = "https://mashape-community-urban-dictionary.p.rapidapi.com"


class DefineEndpoint(CommunityUrbanDict):
    path = "/define"


if __name__ == "__main__":
    cred = ApiKeyCredential()
    endpoint = DefineEndpoint(cred)
    resp = endpoint.get(query_params={
        "term": "wat",
        })

    # resp here is a Response object from requests module/library
    print(resp.status_code)
    print(resp.content)
```

We added a sample code for this scenario over the `examples/` folder

<!-- TODO add example for aiohttp -->

## License

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

