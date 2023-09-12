import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

time.sleep(5) #здесь и далее приостановка выполнения в секундах

drive = webdriver.Ie(executable_path = r'IEDriverServer.exe') 

drive.get('http://192.168.*.*/') #IP адрес регистратора может быть с номером порта

time.sleep(10) 

drive.find_element(By.ID, 'txtUserName').send_keys('login')  #Ваш логин к регистратору
drive.find_element(By.ID, 'txtPassword').send_keys('Pass') #Пароль к регистратору
drive.find_element(By.ID, 'txtPassword').send_keys(Keys.ENTER) #Иммитация нажатия Enter для перехода на следущую страницу

time.sleep(10)

search1 = drive.find_element(By.ID, 'seg_selector') #открытие вкладки для выбора сетки отображения
drive.execute_script("arguments[0].click();", search1) #иммитация нажатия
search2 = drive.find_element(By.ID, 'seg_9') #выбор сетки 3*3
drive.execute_script("arguments[0].click();", search2) #иммитация нажатия

time.sleep(5)

full = drive.find_element(By.ID, 'full_screen') #выбор кнопки изображения на полный экран
drive.execute_script("arguments[0].click();", full) #иммитация нажатия

drive.close 
drive.quit 