import time
from datetime import datetime
from plyer import notification

deadline = datetime(2024, 9, 17, 22, 00, 00)

def send_reminder():
    notification.notify(
        title = str.upper("Counselor"),
        message = "Evaluation form, Excel sheet, ani transcript",
        timeout = "10"
    )
while datetime.now() < deadline:
    send_reminder()
    time.sleep(14400)

       