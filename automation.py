from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 
import pyautogui as magic 
from datetime import datetime
import sys

#main
def main():
  #infinite loop
  while True:

    now = datetime.now()
    time = now.strftime("%I")

    #runs the code between 9 to 6 
    if int(time) >= 9 and int(time) >=5:
      sleep(5)
      join_class()
      sleep(10)

#Join the class for me 
def join_class() :

  driver = webdriver.Chrome(executable_path='/Users/your path/chromedriver')

  #Login into the institutions website 
  driver.get('institutes website ')

  #maximising the window 
  driver.maximize_window()

  #getting current date & time 
  current_time = datetime.now()
  today_date = current_time.day
  print(today_date)

  now = datetime.now()
  time = now.strftime("%I")
  print(time)
  
  #Entering the username 
  username = driver.find_element_by_xpath('//*[@id="txtusername"]')
  username.send_keys('your own username')
  #Entering the username 
  password = driver.find_element_by_xpath('//*[@id="password"]')
  password.send_keys('your own password')
  
  #logging in
  login_button = driver.find_element_by_xpath('//*[@id="Submit"]')
  login_button.click()

  learn = driver.find_element_by_xpath('//*[@id="Main"]/div[11]/a')
  learn.click()
  
  #switching the window 
  parent_window = driver.current_window_handle
  child_window = driver.window_handles
  for child in child_window:
    if parent_window != child:
      driver.close()
      driver.switch_to.window(child)
      break
  
  # finding online class 
  table = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_GridViewonline"]').text
  count = table.count('Date')

  #Variable required in the code ahead 
  i=0
  class_exisits = 0 


  #joining the class 
  while i < count:
    i=i+1

    #getting the date time and link of class 
    current_class = driver.find_element_by_xpath(f'//*[@id="Content_PlaceHolder1_GridViewonline"]/tbody/tr[{i}]').text
    clickable_link = driver.find_element_by_xpath(f'//*[@id="Content_PlaceHolder1_GridViewonline"]/tbody/tr[{i}]/td/a')

    # Joining the which needs to be joined right now 
    if current_class[7:9] == str(today_date) and current_class[27:29]==time:
      clickable_link.click()
    
      #Shifting to the join window 
      parent_window = driver.current_window_handle
      child_window = driver.window_handles
      for child in child_window:
        if parent_window != child:
          driver.switch_to.window(child)
          break
        
      #opening the app 
      sleep(15)
      magic.moveTo(909,256,duration=1)
      magic.click()

      #joining audio
      sleep(20)
      magic.moveTo(736,400,duration=3)
      magic.click() 

      #waiting in the class 
      sleep(2400)

      #leaving the class 
      magic.moveTo(1395,756,duration=3)
      magic.click() 

      #waiting before we join the again 
      sleep(1500)
      class_exisits = class_exisits +1
      break
    
  #if link does not exist 
  if class_exisits == 0:
    #waiting for 10 mins 
    sleep(600)

    #repeating the process
    while i < count:
      i=i+1
      current_class = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_GridViewonline"]/tbody/tr[{i}]/td/a/div/h6').text
      clickable_link = driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_GridViewonline"]/tbody/tr[{i}]/td/a')
    if current_class[7:9] == str(today_date) and current_class[27:29]==time:
      clickable_link.click()
      parent_window = driver.current_window_handle
      child_window = driver.window_handles
    for child in child_window:
      if parent_window != child:
        driver.switch_to.window(child)
        break

    #opening the app 
    sleep(15)
    magic.moveTo(736,400,duration=3)
    magic.click() 
    #joining audio 
    sleep(20)
    magic.moveTo(736,400,duration=3)
    magic.click() 
    #leaving the app after 40 mins 
    sleep(2400)
    magic.moveTo(1395,756,duration=3)
    magic.click() 

    #waiting before next class 
    sleep(1500)
    class_exisits = class_exisits +1 
    
main()
















