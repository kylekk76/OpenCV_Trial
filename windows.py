import numpy as np
import win32gui, win32ui, win32con
from threading import Thread, Lock

class WindowsCapture:
    
    stopped = True
    lock = None
    screenshot = None
    #properties
    w = 0
    h = 0
    hwnd = None

    def __init__(self,windowname = None):
        self.lock = Lock()
        
        self.w = 1920 # set this
        self.h = 1080 # set this
        # in case we dont pass any windows capture the desktop
        if windowname is None:
            self.hwnd= win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, windowname)
        # Resize the windows
        windows_rect = win32gui.GetWindowRect(self.hwnd)
        self.w= windows_rect[2]-windows_rect[0]
        self.h= windows_rect[3]-windows_rect[1]
        # for this game this crop too much so i gonna modify it
        w_pixels = 270
        h_pixels = 270
        self.w = self.w + w_pixels
        self.h = self.h + h_pixels
        
    def get_screenshot(self):
        
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0 , 0),(self.w , self.h) , dcObj, (0 , 0), win32con.SRCCOPY)
        #grabing the screen
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        #Reshape the image
        img.shape = (self.h , self.w, 4)
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        #Treating the imagen for opencv
        #img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img
    @staticmethod
    def WindowsName():
        def winhandler(hwmd,ctx):
            if win32gui.IsWindowVisible(hwmd):
                print(hex(hwmd),win32gui.GetWindowText(hwmd))
        win32gui.EnumWindows(winhandler, None)

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        screenshot = self.get_screenshot()

        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()
