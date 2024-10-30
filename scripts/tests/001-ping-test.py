from requests import get

def run():
    output = ""

    # Querying Backend
    try:
        response = get("http://localhost:8080/").status_code
        output += f"Backend page \"/\" HTTP code: {response}\n"
    except Exception as e:
        output += f"Could not query backend: {e}\n"
        return (False, output)

    # Querying Frontend
    try:
        response = get("http://localhost:8081/").status_code
        output += f"Frontend page \"/\" HTTP code: {response}\n"
    except Exception as e:
        output += f"Could not query backend: {e}\n"
        return (False, output)

    return (True, output)
