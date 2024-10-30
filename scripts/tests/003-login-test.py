from requests import Session

tests = [
    {"name": "Username empty",
     "test": {
        "username": "",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 404
    },
    {"name": "Username invalid",
     "test": {
        "username": "userdontexists",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 404
    },
    {"name": "Username invalid characters",
     "test": {
        "username": "`~!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 404
    },
    {"name": "Password empty",
     "test": {
        "username": "allgooduser",
        "password": "",
     },
     "expected_code": 401
    },
    {"name": "Password invalid",
     "test": {
        "username": "allgooduser",
        "password": "InvalidPassword",
     },
     "expected_code": 401
    },
    {"name": "Password invalid characters",
     "test": {
        "username": "allgooduser",
        "password": "`~!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\",
     },
     "expected_code": 401
    },
    {"name": "All good",
     "test": {
        "username": "allgooduser",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 200
    },
]

def run():
    output = ""
    s = Session()

    for test in tests:
        print(f"=== Test: {test.get('name')} ===")
        output = s.post("http://localhost:8080/api/register", data=test.get("test"))
        if output.status_code != test.get("expected_code"):
            output += f"Expected error code {test.get('expected_code')} but got {output.status_code}\n"
            return (False, output)
        else:
            output += f"Got expected {output.status_code} error code\n"
    return (True, output)