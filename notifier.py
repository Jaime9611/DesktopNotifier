import time

# python -m pip install win10toast
from win10toast import ToastNotifier


toaster = ToastNotifier()
count = 0


while True:

    count += 1

    if count == 1:
        message = 'Leave the chair.'
    elif count == 2:
        message = 'Drink water.'
    elif count == 3:
        message = 'Come on again.'
    else:
        break

    toaster.show_toast( "Hey!", message, threaded=True,
                    icon_path=None, duration=3)

    # Wait
    time.sleep(4)
