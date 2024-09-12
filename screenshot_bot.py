from PIL import ImageGrab
import time
import keyboard
from plyer import notification

def take_screenshot():

    print("Press 's' for a screenshot and 'q' to quit")

    keyboard.block_key('s')
    keyboard.block_key('q')

    while True:

        if keyboard.is_pressed('s'):
            screenshot = ImageGrab.grab()
            filename = f"screenshot{int(time.time())}.png"
            screenshot.save(filename)

            notification.notify(
                title = "SUCCESS",
                message = f"Screenshot saved as {filename}",
                timeout = 1
            )

            time.sleep(1)

        if keyboard.is_pressed('q'): 
            notification.notify(
                title = "Exiting",
                message = "The bot has stopped running.",
                timeout = 1
            )
            break

            time.sleep(0.1)

if __name__ == "__main__":
    take_screenshot()