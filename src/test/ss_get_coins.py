
import requests

BASE_URL = 'https://shapeshift.io/%s'

def get_coins():
    url_path = 'getcoins'
    url = BASE_URL % url_path
    response = requests.get(url)
    return response.json()

