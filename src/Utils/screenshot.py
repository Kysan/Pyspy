import pyautogui
from .strings import randomString


def takeScreenshot():
    image = pyautogui.screenshot()
    image_path = randomString()+".png"
    image.save(image_path)
    return image_path
