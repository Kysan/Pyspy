import cv2
from .strings import .randomString


# TODO
def listWebcam():
    pass


def takePicture(camID=0):
    # il peut y avoir plusieurs cam

    cam = cv2.VideoCapture(camID)
    # * accomodation à la luminosité ambiante
    for k in range(4):
        cam.read()
    rt, frame = cam.read()
    cam.release()
    fileName = randomString()+".png"
    cv2.imwrite(fileName, frame)
    cam.release()
    return fileName
