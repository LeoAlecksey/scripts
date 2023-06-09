import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

time.sleep(60) #здесь и далее приостановка выполнения в секундах

drive = webdriver.Ie(executable_path = r'IEDriverServer.exe') 

drive.get('http://192.168.*.*/') #IP адрес регистратора может быть с номером порта

time.sleep(15)

drive.find_element(By.ID, 'username').send_keys('log') #Ваш логин к регистратору
drive.find_element(By.ID, 'password').send_keys("pass") #Ваш пароль к регистратору
drive.find_element(By.ID, 'password').send_keys(Keys.ENTER) #Иммитация нажатия Enter для перехода на следущую страницу

time.sleep(10)

search = drive.find_element(By.CLASS_NAME, 'icon-playall') #выбор кнопки воспроизведения изображения
drive.execute_script("arguments[0].click();", search) #иммитация нажатия

time.sleep(5)

full = drive.find_element(By.CLASS_NAME, 'icon-full') #выбор кнопки изображения на полный экран
drive.execute_script("arguments[0].click();", full) #иммитация нажатия

drive.close
drive.quit