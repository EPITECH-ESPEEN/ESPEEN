from ._run_tests import run_test

tests = [
    {"name": "Username empty",
     "login": False,
     "method": "POST",
     "url": "/api/register",
     "json": {
        "username": "",
        "email": "invalid.username@testing.me",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "tests": [
        {
            "type": "code",
            "value": 500
        }
     ]
    },

    {"name": "Email empty",
     "login": False,
     "method": "POST",
     "url": "/api/register",
     "json": {
        "username": "invalidemail",
        "email": "",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "tests": [
        {
            "type": "code",
            "value": 500
        }
     ]
    },

    {"name": "Password empty",
     "login": False,
     "method": "POST",
     "url": "/api/register",
     "json": {
        "username": "invalidpassword",
        "email": "invalid.password@testing.me",
        "password": "",
     },
     "tests": [
        {
            "type": "code",
            "value": 500
        }
     ]
    },

    {"name": "All good",
     "login": False,
     "method": "POST",
     "url": "/api/register",
     "json": {
        "username": "allgooduser",
        "email": "all.good.user@testing.me",
        "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
     },
     "tests": [
        {
            "type": "code",
            "value": 200
        }
     ]
    }
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
