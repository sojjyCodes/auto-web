from selenium import webdriver
operation = input('''
what browser do you want to use to perform this task 
1 for Chrome
2 for Firefox
''')

if operation == '1':

    driver = webdriver.Chrome()
    driver.get("https://www.github.com/sojjyCodes")

else:
    if operation == '2':
        driver2 = webdriver.Firefox()
        driver2.get("https://www.facebook.com")
