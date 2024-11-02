from ._run_tests import run_test

user = {
    "username": "allgooduser",
    "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
}

def run():
    return run_test({
        "name": "Removing user",
        "login": True,
        "method": "DELETE",
        "url": "/api/user",
        "json": user,
        "tests": [
            {
                "type": "contains",
                "value": "User deleted successfully"
            }
        ]
    })