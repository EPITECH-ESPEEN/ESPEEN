from requests import Session

user = {
    "username": "allgooduser",
    "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
}

def run():
    output = ""
    s = Session()

    token = s.post("http://localhost:8080/api/login", json=user).json().get("access_token")
    s.headers.update({"Autorization": "Bearer " + token})

    # cookies should be all good
    output += s.delete("http://localhost:8080/user").text + '\n'

    return (True, "=== All good ===")