from ._run_tests import run_test

def run():
    return run_test({
        "name": "Verify that new user doesn't contains oauth tokens",
        "login": True,
        "method": "GET",
        "url": "/api/oauth",
        "tests": [
            {
                "type": "code",
                "value": 404,
            },
            {
                "type": "json",
                "value": {
                    "error": "^Service not found$"
                }
            }
        ]
    })