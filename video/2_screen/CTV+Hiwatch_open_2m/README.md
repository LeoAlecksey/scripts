Автозапуск видеостены на 2-х мониторах через web-морду регисраторов CTV + HiWatch или Hikvision.
1. В файле'secure.txt' написать 'login=password' без кавычек. (при условии использования 
одинаковых лоогина и пароля, в ином случаае правьте secure.py и тело основной программы в местах логина open_cam_2_monitor.py)
2. В файле 'object.txt' указать 2 строки без пробелов (название объекта и адррес сервера с портом если есть NAT)
первая строка данных для регистратора CTV вторая HiWatch или Hikvision: 
'name=https:\\192.168.1.1:80' без кавычек.



Python 3.9.13
pyinstaller 4.4

Зависимости:
time
os
requests
speedtest
selenium v.3.141.0
secure # добавленный handler
object # добавленный handler

компиляция:

python3.9 -m PyInstaller --noconfirm --onedir --console --icon "C:/.../GIT_repos/work_Scripts/Video/CTV+Hiwatch_open_2m/result_GMRpFcL.ico" --add-data "C:/.../GIT_repos/work_Scripts/Video/CTV+Hiwatch_open_2m/IEDriverServer.exe;." --add-data "C:/.../GIT_repos/work_Scripts/Video/CTV+Hiwatch_open_2m/secure/object.txt;." --add-data "C:/.../GIT_repos/work_Scripts/Video/CTV+Hiwatch_open_2m/secure/secure.txt;." --add-data "C:/.../GIT_repos/work_Scripts/Video/CTV+Hiwatch_open_2m/LICENCE.md;." --add-data "C:/.../GIT_repos/work_Scripts/Video/CTV+Hiwatch_open_2m/README.md;."  "C:/.../GIT_repos/work_Scripts/Video/CTV+Hiwatch_open_2m/open_cam_2_monitor.py"

