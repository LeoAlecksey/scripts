import cv2
from art import tprint

while True:

    def main():

        # URI потока RTSP
        rtsp_url = "rtsp://login:pass@192.168.70.41:554/Streaming/Channels/101"

        # Открытие потока RTSP
        cap = cv2.VideoCapture(rtsp_url)

        # Проверка, открыт ли поток RTSP
        if not cap.isOpened():
            print("Не удалось открыть поток RTSP")
            exit()
        cv2.namedWindow("RTSP Stream", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("RTSP Stream", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Чтение кадров из потока RTSP
        while True:
            ret, frame = cap.read()
            # Проверка, успешно ли прочитан кадр
            if ret:
                # Обработка кадра здесь
                cv2.imshow("RTSP Stream", frame)
            # Ожидание нажатия пользователем клавиши «q» для выхода
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Не удалось прочитать кадр из потока RTSP")

        # Освобождение потока RTSP и закрытие окна
        cap.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        
        print('developed by')
        tprint("@LeoAlecksey", font="cybermedium")
        print(f'/nhttps://github.com/LeoAlecksey/LeoAlecksey')
        
        main()
