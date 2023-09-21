# Updated: 9/20/23, Author: Connor
import pyautogui
import json
from selenium import *

#Config
JsonDir = "config.json"
Config = []
with open(JsonDir, 'r') as file:
    Config = json.load(file)
Url = Config["Url"]
WebDriverDir = Config["Driver"]
WPM = Config["WPM"]
WPS = WPM/60

#Main
def Run():
    print("Running")

#Loop
while True:
    try: 
        print("Running at WPM of ",str(WPM))
        Run()
    except Exception as Error:
        print("Error Occoured: ",Error)