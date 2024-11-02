from requests import Response, Session
from ._authenticate import login
import re

BASE_URL = "http://localhost:8080"

def compare_json_regex(ref, expect):
    if type(ref) != type(expect):
        return (False, f"== Expected type {type(expect)} but got {type(ref)}\n")
    if type(expect) == dict:
        for k, v in expect.items():
            status, output = compare_json_regex(ref.get(k), v)
            if not status:
                return (False, output)
    elif type(expect) == list:
        for _expect in expect:
            status = False
            for _ref in ref:
                if compare_json_regex(_ref, _expect)[0]:
                    status = True
                    break
            if not status:
                return (False, f"== {_expect} not found in {ref}")
    else:
        _ref = type(expect)(ref)
        if type(expect) == str:
            if not re.search(expect, _ref):
                return (False, f"== Regex {expect} not found in {_ref}\n")
        else:
            if expect != _ref:
                return (False, f"== {_ref} != {expect}")
    return (True, "== Ref matches expected")

def run_test(test: dict):
    output = ""
    status = True
    s = Session()
    if test.get("login"):
        s = login()

    output += f"== {test.get('name')} ==\n"

    response: Response =  s.request(
        method=test.get("method"),
        url=BASE_URL + test.get("url"),
        json=test.get("json") or {},
        headers=test.get("headers") or {},
        cookies=test.get("cookies") or {},
    )

    for expect in test.get("tests"):
        if expect.get("type") == "code":
            if response.status_code != expect.get("value"):
                output += f"== Expected error code {expect.get('value')} but got {response.status_code}\n"
                status = False
                break
            else:
                output += f"== Got expected status code {response.status_code}\n"
        elif expect.get("type") == "contains":
            if not expect.get("value") in response.text:
                output += f"== Expected response to contain \"{expect.get('value')}\" but it was not found\n"
                status = False
                break
            else:
                output += f"== Output contains \"{expect.get('value')}\"\n"
        elif expect.get("type") == "json":
            json = response.json()
            status, _output = compare_json_regex(json, expect.get("value"))
            output += _output
        else:
            return (False, f"== Test type {expect.get('type')} not found\n")

    output += '\n'
    return (status, output)