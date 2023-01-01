from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "path/to/your/chrome/driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("link to the TypeRacer race")

while True:
    try:
        driver.find_element(By.LINK_TEXT, "Join race").click() #presses join race button
    except:
        time.sleep(1)
    else:
        break

time.sleep(2)

#gets sentence
first_letter = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]').text
rest_of_first_word = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]').text

rest_of_the_sentence = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]').text

sentence = f"{first_letter}{rest_of_first_word} {rest_of_the_sentence}"
# print(sentence)

input("Press enter when you want me to start typing!")

#finds input box and starts typing
text_input = driver.find_element(By.CLASS_NAME, 'txtInput')

for char in sentence:
    text_input.send_keys(char)
    time.sleep(0.05)


time.sleep(50000)
driver.close()
