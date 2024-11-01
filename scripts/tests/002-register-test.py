from requests import Session

tests = [
    {"name": "Username empty",
     "test": {
        "username": "",
        "email": "invalid.username@testing.me",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 500
    },
    {"name": "Email empty",
     "test": {
        "username": "invalidemail",
        "email": "",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 500
    },
    {"name": "Password empty",
     "test": {
        "username": "invalidpassword",
        "email": "invalid.password@testing.me",
        "password": "",
     },
     "expected_code": 500
    },
    {"name": "All good",
     "test": {
        "username": "allgooduser",
        "email": "all.good.user@testing.me",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 200
    },
]

def run():
    output = ""
    s = Session()

    for test in tests:
        output += f"=== Test: {test.get('name')} ===\n"
        request = s.post("http://localhost:8080/api/register", json=test.get("test"))
        if request.status_code != test.get("expected_code"):
            output += f"Expected error code {test.get('expected_code')} but got {request.status_code}\n"
            output += f"Content: \n{request.text}\n"
            return (False, output)
        else:
            output += f"Got expected {request.status_code} error code\n"
    return (True, output)
