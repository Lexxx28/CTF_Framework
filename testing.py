import requests

x = requests.Session()
url = "http://127.0.0.1:8000"

def register():
    url_full = url + "/register/"
    data = {
        "username":"testinagga",
        "password":"PasswordS123",
        "email":"testingaga@gmail.com",
    }
    res = x.post(url_full, json=data)
    print(res.text)
    
def login():
    url_full = url + "/login/"
    data = {
        "username":"testinagga",
        "password":"PasswordS123",
    }
    res = x.post(url_full, json=data)
    print(res.text)
    print(res.cookies)
    

def create_challenge():
    url_full = url + "/challenges/"
    data = {
        "title":"wkwk",
        "description":"wkwk",
        "points":400,
        "category":"forensics",
        "difficulty":"easy",
        "attachment":"lol"
    }
    res = x.post(url_full, json=data)
    print(res.text)

def view_challenge(id):
    url_full = url + "/challenges/" + f"?id={id}&category=forensics"
    res = x.get(url_full)
    print(res.text)

register()
login()
create_challenge()
view_challenge(1)