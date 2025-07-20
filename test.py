import requests

BASE_URL = "http://127.0.0.1:8001"
RAPIDAPI_HEADER = {"x-rapidapi-host": "testhost"}


def test_ping():
    print("Test /ping :", requests.get(f"{BASE_URL}/ping").json())

def test_accueil():
    print("Test / :", requests.get(f"{BASE_URL}/").json())

def test_detect_get():
    params = {"text": "Bonjour, comment ça va ?"}
    r = requests.get(f"{BASE_URL}/detect", params=params, headers=RAPIDAPI_HEADER)
    print("Test /detect GET :", r.json())

def test_detect_post():
    data = {"text": "Hello, how are you?"}
    r = requests.post(f"{BASE_URL}/detect", json=data, headers=RAPIDAPI_HEADER)
    print("Test /detect POST :", r.json())

def test_translate_get():
    params = {"text": "Bonjour", "target": "en"}
    r = requests.get(f"{BASE_URL}/translate", params=params, headers=RAPIDAPI_HEADER)
    print("Test /translate GET :", r.json())

def test_translate_post():
    data = {"text": "Hello", "target": "fr"}
    r = requests.post(f"{BASE_URL}/translate", json=data, headers=RAPIDAPI_HEADER)
    print("Test /translate POST :", r.json())

def test_detect_translate_get():
    params = {"text": "Bonjour", "target": "en"}
    r = requests.get(f"{BASE_URL}/detect-translate", params=params, headers=RAPIDAPI_HEADER)
    print("Test /detect-translate GET :", r.json())

def test_detect_translate_post():
    data = {"text": "Hello", "target": "fr"}
    r = requests.post(f"{BASE_URL}/detect-translate", json=data, headers=RAPIDAPI_HEADER)
    print("Test /detect-translate POST :", r.json())

def test_detect_translate_get_noheader():
    params = {"text": "Bonjour", "target": "en"}
    r = requests.get(f"{BASE_URL}/detect-translate", params=params)
    print("Test /detect-translate GET sans header :", r.json())

def test_detect_translate_post_noheader():
    data = {"text": "Hello", "target": "fr"}
    r = requests.post(f"{BASE_URL}/detect-translate", json=data)
    print("Test /detect-translate POST sans header :", r.json())

def test_detect_get_noheader():
    params = {"text": "Bonjour"}
    r = requests.get(f"{BASE_URL}/detect", params=params)
    print("Test /detect GET sans header :", r.json())

def test_translate_post_noheader():
    data = {"text": "Hello", "target": "fr"}
    r = requests.post(f"{BASE_URL}/translate", json=data)
    print("Test /translate POST sans header :", r.json())

if __name__ == "__main__":
    test_ping()
    test_accueil()
    test_detect_get()
    test_detect_post()
    test_translate_get()
    test_translate_post()
    test_detect_translate_get()
    test_detect_translate_post()
    test_detect_get_noheader()
    test_translate_post_noheader()
    test_detect_translate_get_noheader()
    test_detect_translate_post_noheader() 