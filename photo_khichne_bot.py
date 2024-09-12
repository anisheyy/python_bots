import cv2
import time

def capture_photo():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("camera did not open successfully.")
        return
    
    print("Press 'c' to capture and 'q' to exit the camera")
    
    while True:
        ret, frame = cam.read()

        frame = cv2.flip(frame, 1)

        cv2.imshow("anish_ko_camera", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("c"):
            filename = f"image{int(time.time())}.png"
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}")
        
        elif key == ord("q"):
            print("Exiting...")
            break

    cam.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    capture_photo()




        









