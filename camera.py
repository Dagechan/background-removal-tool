from rembg import remove
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
start_time = time.time()

def shot_COUNTER(interval):
    if interval <= 10:
        return "number_1"
    elif interval <= 20:
        return "number_2"
    elif interval <= 30:
        return "number_3" 

def removeBG():
    save_interval = 10  # 保存間隔（秒）
    while True:
        ret, frame = cap.read()

        current_time = time.time() 

        # テキスト分岐
        text_to_show = shot_COUNTER(save_interval)
        
        # テキスト描画
        cv2.putText(frame, text_to_show, (29, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3, cv2.LINE_AA)

        
        # カメラ映像と処理後の画像を表示
        #cv2.imshow('Camera', cv2.flip(frame, 1))
        cv2.imshow('Camera', frame)

        # 一定の時間が経過したらprocessed_frameを保存してアプリを終了
        if current_time - start_time >= save_interval:
            # rembgで背景を除去
            processed_frame = remove(frame)
            save_filename = f"processed_frame_{int(current_time)}.png"
            # cv2.imwrite(save_filename, processed_frame)
            cv2.imwrite('./Image/'+ save_filename, processed_frame)
            # print(f"Processed frame saved as {save_filename}")
            save_interval += 10
            if save_interval > 30:
                break

        # ESCキーでアプリを終了
        key = cv2.waitKey(10)
        if key == 27:
            break


if __name__ == '__main__':
    removeBG()
    cap.release()
    cv2.destroyAllWindows()
