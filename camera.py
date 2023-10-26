from rembg import remove
import playsound
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
start_time = time.time()

right_click = False


# def shot_COUNTER(interval):
#     if interval <= 10:
#         return "number_1"
#     elif interval <= 20:
#         return "number_2"
#     elif interval <= 30:
#         return "number_3"

def onMouseClick(event, x, y, flags, param):
    global right_click

    right_click = False

    if event == cv2.EVENT_LBUTTONDOWN:
        print('左クリックされました')
        right_click = True


def removeBG():
    cnt = 0
    save_interval = 10  # 保存間隔（秒）
    while True:
        ret, frame = cap.read()

        current_time = time.time()

        # # テキスト分岐
        # text_to_show = shot_COUNTER(save_interval)
        text_to_show = "Click to shot : " + str(cnt + 1)

        # # テキスト描画
        cv2.putText(frame, text_to_show, (29, 50),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3, cv2.LINE_AA)

        # カメラ映像と処理後の画像を表示
        # cv2.imshow('Camera', cv2.flip(frame, 1))
        cv2.imshow('Camera', frame)

        cv2.setMouseCallback('Camera', onMouseClick)

        # 一定の時間が経過したらprocessed_frameを保存してアプリを終了
        if right_click == True:
            playsound.playsound('./SE/Camera-Phone01-1.mp3')
            # rembgで背景を除去
            processed_frame = remove(frame)
            save_filename = f"processed_frame_{int(current_time)}.png"
            # cv2.imwrite(save_filename, processed_frame)
            cv2.imwrite('./Image/' + save_filename, processed_frame)
            # print(f"Processed frame saved as {save_filename}")
            cnt += 1
            if cnt == 3:
                break

        # ESCキーでアプリを終了
        key = cv2.waitKey(10)
        if key == 27:
            break


if __name__ == '__main__':
    removeBG()
    cap.release()
    cv2.destroyAllWindows()
