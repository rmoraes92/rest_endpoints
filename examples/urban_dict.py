import sys
from endpoints import Credential
from endpoints import Endpoint


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
    if len(sys.argv) == 3:
        term = sys.argv[1]
        how_many_defs = int(sys.argv[2])

        cred = ApiKeyCredential()
        endpoint = DefineEndpoint(cred)
        resp = endpoint.get(query_params={
            "term": term,
            })

        print('{} Definitions for "{}":'.format(how_many_defs, term))
        for definition in resp.json()["list"][:how_many_defs]:
            print("\t- {}".format(definition["definition"]))
    else:
        print("Usage: python urban_dict.py [word] [num_of_def]")
        print("Example: python urban_dict.py wat 2")
