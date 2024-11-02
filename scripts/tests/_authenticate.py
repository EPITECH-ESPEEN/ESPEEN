from requests import Session

user = {
    "username": "allgooduser",
    "password": "Th1s1s4L*ng4ndVal1dP4ssw0rd!",
}

def login():
    s = Session()

    token = s.post("http://localhost:8080/api/login", json=user).json().get("access_token")
    s.headers.update({"Authorization": "Bearer " + token})

    return s