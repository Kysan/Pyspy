import pyautogui
from .strings import randomString


def makeScreenshot():
    image = pyautogui.screenshot()
    image_path = randomString()+".png"
    image.save(image_path)
    return image_path
