#Created by sojjyCodes.
from selenium import webdriver
import pyttsx3
import time
operation = input('''
what browser do you want to use to perform this task 
1 for Chrome
2 for Firefox
''')

if operation == '1':
    print("Opening Chrome ")
    time.sleep(3)
    pyttsx3.speak("Opening, Chrome")
    driver = webdriver.Chrome()
    driver.get("https://www.github.com/sojjyCodes")

elif operation == '2':
        print("Opening Firefox")
        time.sleep(3) 
        pyttsx3.speak("Opening Firefox")
        driver2 = webdriver.Firefox()
        driver2.get("https://www.facebook.com")

else:
    pyttsx3.speak("Invalid,inpute") #Spelling "inpute" was  intentional. if he wa to speak input it will come out wrong.
    print("Invalid input")

