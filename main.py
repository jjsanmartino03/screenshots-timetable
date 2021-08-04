import pyautogui
import json
from pprint import pprint


with open('config.json') as f:
  data = json.load(f)

pprint(data['data'])