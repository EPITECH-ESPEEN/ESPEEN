from requests import get
from time import sleep

def run():
    output = ""
    backend_up = False
    frontend_up = False


    # Querying backend and frontend until they're up

    while any((not backend_up, not frontend_up)):
        if not backend_up:
            try:
                response = get("http://localhost:8080/").status_code
                output += f"Backend page \"/\" HTTP code: {response}\n"
            except Exception as e:
                output += f"Could not query backend: {e}\n"
            else:
                backend_up = True

        if not frontend_up:
            try:
                response = get("http://localhost:8081/").status_code
                output += f"Frontend page \"/\" HTTP code: {response}\n"
            except Exception as e:
                output += f"Could not query backend: {e}\n"
            else:
                frontend_up = True
        if any((not backend_up, not frontend_up)):
            sleep(5)

    return (True, output)
