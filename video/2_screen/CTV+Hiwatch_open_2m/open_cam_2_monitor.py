import time
import os
import requests
import speedtest
import selenium
from os import system
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import object
import secure




while True:

    #Тест скорости и соединения.
    
    print("Проверка соединения")

    response1 = requests.get(object.adress1)
    print(object.ob1, " статус:", response1.status_code)

    response2 = requests.get(object.adress2)
    print(object.ob2, " статус:", response2.status_code)


    print("Тест скорости соединения")
    st  = speedtest.Speedtest()
    down1 = st.download()/1048576
    up1 = st.download()/1048576
    print("Скорость соединения c интернетом")
    print("Скорость закрузки = ", round(down1, 2))
    print("Скорость отдачи = ", round(up1, 2))
    
    options = webdriver.IeOptions()
    options.ignore_zoom_level = True
    options.ignore_protected_mode_settings = True
    path = r'IEDriverServer.exe'
    drive = webdriver.Ie(executable_path = path, options=options).set_window_position(2000, 0)
    

    #функции вывода на экран 1 видеостены

    def open1():

        drive = webdriver.Ie(executable_path = path, options=options)
        drive.set_window_position(-2000, 0)
        drive.get(object.adress1)
        
        time.sleep(5) #здесь и далее приостановка выполнения в секундах

        drive.get(object.adress1) 

        time.sleep(10) 

        drive.find_element(By.ID, 'txtUserName').send_keys(secure.login) 
        drive.find_element(By.ID, 'txtPassword').send_keys(secure.password) 
        drive.find_element(By.ID, 'txtPassword').send_keys(Keys.ENTER) 
        time.sleep(10)

        search1 = drive.find_element(By.ID, 'seg_selector') 
        drive.execute_script("arguments[0].click();", search1) 
        search2 = drive.find_element(By.ID, 'seg_9') 
        drive.execute_script("arguments[0].click();", search2)

        time.sleep(5)

        full = drive.find_element(By.ID, 'full_screen')
        drive.execute_script("arguments[0].click();", full) 


        time.sleep(10)
        drive.close

        
    #функции вывода на экран 2 видеостены
    
    def open2():

        drive = webdriver.Ie(executable_path = path, options=options)
        drive.set_window_position(2000, 0)
        drive.get(object.adress2)
        
        time.sleep(10)
        drive.find_element(By.ID, 'username').send_keys(secure.login)

        drive.find_element(By.ID, 'password').send_keys(secure.password)

        drive.find_element(By.ID, 'password').send_keys(Keys.ENTER)


        time.sleep(10)
        search = drive.find_element(By.CLASS_NAME, 'icon-playall')
        drive.execute_script("arguments[0].click();", search)

        time.sleep(5)
        full = drive.find_element(By.CLASS_NAME, 'icon-full')
        drive.execute_script("arguments[0].click();", full)


        time.sleep(10)
        drive.close
        

    #Запуск основной программы

    print("Запуск видеонаблюдения. Ожидайте...")

    try:

        if up1 > 5 and down1 > 5:
            if response1.status_code == 200 and response2.status_code == 200:
                print('системы видеонаблюдения в норме')
                open1()
                open2()
                time.sleep(3600)
                
            
            
            elif response1.status_code != 200 and response2.status_code == 200:
                
                print(f'Системы видеонаблюдения {object.ob1} - Недоступны!\n Системы видеонаблюдения {object.ob2} будут запущены!.\n\n\n Обратитесь к системному администратору для устранения неполадки.')
                open2()
                time.sleep(3600)
                


            elif response2.status_code != 200 and response1.status_code == 200:
                
                print(f'Системы видеонаблюдения {object.ob2} - Недоступны!\n Системы видеонаблюдения {object.ob1} будут запущены!.\n\n\n Обратитесь к системному администратору для устранения неполадки.')
                open1()
                time.sleep(3600)
            
            else :
                print('Системы видеонаблюдения не доступны! Обратитесь к системному администратору.')

        else:
            print("Итернет соединение слабое или отсутствует. Програма будет запущена по восстановлении соединения.")
            time.sleep(60)

    finally:
        print('Ошибка! Свяжитесь с системным администратором')

    os.system("taskkill /im iexplore.exe")
    print("Перезапуск системы")
    time.sleep(60)


