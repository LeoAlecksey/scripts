import subprocess
import os
import getpass
from art import tprint
from dotenv import load_dotenv
import time 
import tqdm

#---------------      объявление переменных окружения



dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

vpn_address = os.getenv("VPNADRESS")
vpn_name = os.getenv("VPNNAME")
vpn_psk = os.getenv("PSK")
domain =os.getenv("DOMAIN")

#---------------      Основная программа
def main():
   
    #---------------      подпись
   
    print('developed by')
    tprint("@LeoAlecksey", font="cybermedium")
    print(f'https://github.com/LeoAlecksey/LeoAlecksey')
    
    #---------------      индикация выполнения
    
    print('\nУстанавливаем и настраиваем VPN...')
    for _ in tqdm.tqdm(range(100)):
        time.sleep(0.05)

    #---------------      выполнение команды powershell, добавление VPN с заданными параметрами

    subprocess.run('powershell -command add-vpnconnection -Name "$env:VPNNAME" -ServerAddress "$env:VPNADRESS" -TunnelType "L2tp" -AuthenticationMethod MsChapv2 -L2tpPsk "$env:PSK"  -PassThru"')


    print('VPN установлен. Давайте добавим пользователя...')
    time.sleep(2)

    #---------------      запрос данных пользователя

    print('\nВведите логин:')
    login = input(str())

    print('\nВведите пароль VPN:')
    passwordvpn = input(str())

    #---------------      создание .bat файла для запуска VPN c рабочего стола

    USER_NAME = getpass.getuser()

    path = r'C:\Users\%s\Desktop\VPN.bat' % USER_NAME

    file = open(path, 'w') 
    file.write(f'rasdial digniori {login} {passwordvpn}')
    file.close()

    print('VPN - готов к использованию')
    time.sleep(3)
    
    os.system("taskkill /im cmd.exe")

if __name__=='__main__':
    main()