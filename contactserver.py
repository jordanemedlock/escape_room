import requests


SERVER = "http://10.0.0.100:8000" # TODO(JEM): configure

def send_strike():
    r = requests.get(SERVER + "/send/strike")
    return r.json()

def open_door():
    r = requests.get(SERVER + "/open/door")
    return r.json()

def diffuse_bomb():
    r = requests.get(SERVER + "/diffuse/bomb")
    return r.json()

def open_map():
    r = requests.get(SERVER + "/open/map")
    return r.json()
