# Updated: 9/20/23, Author: Connor
import pyautogui
import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
GameDelay = int(Config["Delay"])
SpaceChar = Config["Space"]
TimeoutDelay = int(Config["Timeout"])
StartDelay = int(Config["StartDelay"])
KeyDelay = int(Config["KeyDelay"])

#Browser Interface
Options = webdriver.EdgeOptions()
Options.binary_location=BinaryDir
Options.add_argument("start-maximized")
Options.add_argument("disable-extensions")
Options.add_argument("disable-notifications")
Options.add_argument("disable-logging")
Browser = webdriver.Edge(options=Options)
#Element Names
DashLetter = ".dash-letter"
Retracting = ".is-retracting"
#Main
def Exists(ClassName):
    try:
        if Browser.find_element(By.CSS_SELECTOR,ClassName):
            return True
    except (Exception,NoSuchElementException):
        return False
def SetUp():
    Browser.get(Url)
def Run():
    print("Running")
    for Item in Browser.find_elements(By.TAG_NAME,"input"):
        if Item.get_attribute("type") == "checkbox":
            print("Capcha")
    if Exists(DashLetter) == False:
        Wait = WebDriverWait(Browser,TimeoutDelay)
        Wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,DashLetter)))
    Elements = Browser.find_elements(By.CSS_SELECTOR,DashLetter)
    Elements.pop()
    Words = []
    TextString = ""
    for Element in Elements:
        Text = Element.get_attribute("textContent")
        if SpaceChar in Text:
            Text = str(Text).replace(SpaceChar," ")
            print("SpaceChar")
        Words.append(Text)
        #Words.append(" ")
    if Exists(Retracting):
        Wait = WebDriverWait(Browser,TimeoutDelay)
        Wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,Retracting)))
        time.sleep(StartDelay)
    pyautogui.leftClick()
    for Word in Words:
        TextString = TextString+str(Word)
        '''
        Letters = str(Word).split()
        for Letter in Letters:
            Cap = str(Letter).upper()
            if Cap == Letter:
                pyautogui.hotkey("shift",Letter.lower())
            else:
                print()
        '''
    print("Writing: ",TextString)
    TextString = str(TextString)
    NewString = ""
    Map = [
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",","
    ]
    Index = -1
    for Char in TextString:
        Index = Index+1
        Found = False
        for MapItem in Map:
            LowerChar = Char.lower()
            if MapItem == LowerChar:
                Found = True
                if LowerChar == Char:
                    NewString = NewString + MapItem
                else:
                    #jif Char == ".":
                        #NewString = NewString + "."
                    #elif Char == ",":
                        #NewString = NewString + ","
                    #else:
                        NewString = NewString + MapItem.upper()
        if Found == False:
            if Index != 0:
                #print("a")
                NewString = NewString + " "
    print("Formatted: ",NewString)
    for Char in NewString:
        Upper = Char.upper()
        pyautogui.typewrite(".")
        pyautogui.leftClick()
        if Upper == Char:
            pyautogui.hotkey("shift",Char.lower())
        else:
            pyautogui.typewrite(Char)
        if Char == " ":
            pyautogui.typewrite(" ")
        elif Char == ">":
            pyautogui.typewrite(".")
        time.sleep(KeyDelay)
    #pyautogui.write(NewString,interval=KeyDelay)
    print("Finished")
    Browser.execute("location.reload()")
    #Browser.close()
   # Browser.close()
#Loop
def MainLoop():
    while True:
        try: 
            print("Running at WPM of ",str(WPM))
            SetUp()
            #Run()
            time.sleep(GameDelay)
        except Exception as Error:
            print("Error Occoured: ",Error)
            break
SetUp()
MainLoop()
#Run()