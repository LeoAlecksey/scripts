Скрипт выводит поток видео с вызывной панели домофонной IP системы hiwatch.
Создавался для Rasberry pi4 - который в свою очередь выполняет функцию видеоглазка.
компиляция:

pyinstaller --noconfirm --onefile --console --icon "/result_GMRpFcL.ico" --add-data "/LICENCE.md;." --add-data "/README.md;."  "/main.py"
