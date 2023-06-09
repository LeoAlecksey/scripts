Программу следует конвертировать следующим образом:

pyinstaller --noconfirm --onedir --console --add-data "C:/Users/!Ваш путь к этой папке!/IEDriverServer.exe;."  "C:/Users/!Ваш путь к этой папке!/open_cam_2_monitor.py"

Сборка содержится в папке dist, которая находится в одной директории с папкой venv.