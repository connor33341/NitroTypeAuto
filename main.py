# Updated: 9/20/23, Author: Connor
import pyautogui
import json
import time
from selenium import webdriver

#Config
JsonDir = "config.json"
Config = []
with open(JsonDir, 'r') as file:
    Config = json.load(file)
Url = Config["Url"]
WebDriverDir = Config["Driver"]
BinaryDir = Config["Location"]
WPM = int(Config["WPM"])
WPS = WPM/60

#Browser Interface
Options = webdriver.EdgeOptions()
Options.binary_location=BinaryDir
Browser = webdriver.Edge(options=Options)
#Main
def Run():
    print("Running")
    time.sleep(4)
#Loop
while True:
    try: 
        print("Running at WPM of ",str(WPM))
        Run()
    except Exception as Error:
        print("Error Occoured: ",Error)