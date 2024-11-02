from requests import Session
from datetime import datetime
from time import sleep

def run():
    output = ""
    s = Session()

    output += "=== Testing valid current timestamp ===\n"

    start_timestamp = round(datetime.now().timestamp())
    output += f"== Starting timestamp: {start_timestamp}\n"

    sleep(3)

    server_timestamp = s.get("http://localhost:8080/about.json").json().get("server").get("current_time")
    output += f"== Sever timestamp: {server_timestamp}\n"

    sleep(3)

    end_timestamp = round(datetime.now().timestamp())
    output += f"== Sever timestamp: {end_timestamp}\n"

    if not (start_timestamp < server_timestamp < end_timestamp):
        output += f"== Assert invalid: {start_timestamp} < {server_timestamp} < {end_timestamp}\n"
        return (False, output)

    output += "== All good !\n"

    return (True, output)
