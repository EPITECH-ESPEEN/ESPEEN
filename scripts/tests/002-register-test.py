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
    {"name": "Username too short",
     "test": {
        "username": "u",
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
    {"name": "Email invalid",
     "test": {
        "username": "invalidemail",
        "email": "dont.mind.me.ime.an.email",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "expected_code": 500
    },
    {"name": "Email domain name invalid",
     "test": {
        "username": "invalidemail",
        "email": "invalid.email@n.a",
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
    {"name": "Password bad",
     "test": {
        "username": "invalidpassword",
        "email": "invalid.password@testing.me",
        "password": "password",
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
        print(f"=== Test: {test.get('name')} ===")
        output = s.post("http://localhost:8080/api/register", data=test.get("test"))
        if output.status_code != test.get("expected_code"):
            output += f"Expected error code {test.get('expected_code')} but got {output.status_code}\n"
            return (False, output)
        else:
            output += f"Got expected {output.status_code} error code\n"
    return (True, output)