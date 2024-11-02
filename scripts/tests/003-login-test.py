from ._run_tests import run_test

tests = [
    {"name": "Username empty",
     "login": False,
     "method": "POST",
     "url": "/api/login",
     "json": {
        "username": "",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "tests": [
        {
            "type": "code",
            "value": 404
        }
     ]
    },

    {"name": "Username invalid",
     "login": False,
     "method": "POST",
     "url": "/api/login",
     "json": {
        "username": "userdontexists",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "tests": [
        {
            "type": "code",
            "value": 404
        }
     ]
    },

    {"name": "Password empty",
     "login": False,
     "method": "POST",
     "url": "/api/login",
     "json": {
        "username": "allgooduser",
        "password": "",
     },
     "tests": [
        {
            "type": "code",
            "value": 401
        }
     ]
    },

    {"name": "Password invalid",
     "login": False,
     "method": "POST",
     "url": "/api/login",
     "json": {
        "username": "allgooduser",
        "password": "InvalidPassword",
     },
     "tests": [
        {
            "type": "code",
            "value": 401
        }
     ]
    },

    {"name": "All good",
     "login": False,
     "method": "POST",
     "url": "/api/login",
     "json": {
        "username": "allgooduser",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "tests": [
        {
            "type": "code",
            "value": 200
        }
     ]
    },
]

def run():
    output = ""

    for test in tests:
        status, _output = run_test(test)
        output += _output
        output += '\n'
        if not status:
            return (False, output)
    return (True, output)