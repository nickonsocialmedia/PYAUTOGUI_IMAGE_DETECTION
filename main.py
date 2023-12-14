import pyautogui as pt


# Helper function
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateOnScreen(image, 3, confidence=.7)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=1)  # move to and speed
        pt.moveRel(off_x, off_y, duration=.4)  # adjust and speed
        pt.click(clicks=clicks, interval=.3)


#  sleep(3) leaving sleep optional
nav_to_image('images/image1.png', 1)
