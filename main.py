import cv2 as cv
from time import time
from windows import WindowsCapture
from view import Vision
from threading import Thread
from object_dectection import Detection


windows=WindowsCapture("Gameloop")
#object detection
detector = Detection("Cascade\cascade.xml")
vision_target = Vision(None)
# WindowsCapture.WindowsName()
# exit()
windows.start()
detector.start()

loop_time = time()
while(True):
    if windows.screenshot is None:
        continue

    #Object detection
    detector.update(windows.screenshot)
    # Draw results in the original Image
    detection = vision_target.draw_rectangles(windows.screenshot, detector.rectangles)
    cv.imshow("Computer Vision", windows.screenshot)

    #debug
    print("FPS {}".format(1/(time() - loop_time)))
    loop_time = time()

    key= cv.waitKey(1)
    if key == ord("q"):
        detector.stop()
        cv.destroyAllWindows()
        break
    # Capture screen:
    elif key == ord("p"):
        cv.imwrite("Positive\{}.jpg".format(loop_time),windows.screenshot)
    elif key == ord("n"):
        cv.imwrite("Negative\{}.jpg".format(loop_time),windows.screenshot)

print("Done")