from ._run_tests import run_test

def run():
    return run_test({
        "name": "Verifying validity of \"actionReaction\" page",
        "login": True,
        "method": "GET",
        "url": "/api/actionReactions",
        "tests": [
            {
                "type": "code",
                "value": 200,
            },
            {
                "type": "json",
                "value": {"actionReactions": []} # Validate that output "actionReactions" contains a list
            }
        ]
    })