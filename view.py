import cv2 as cv
import numpy as np

class Vision:
    # Properties:
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    def __init__(self, needle_path, method = cv.TM_CCOEFF_NORMED):
        if needle_path:
            self.needle_img = cv.imread(needle_path,cv.IMREAD_UNCHANGED)
            # Dimensions
            self.needle_w = self.needle_img.shape[1]
            self.needle_h = self.needle_img.shape[0]
        # Methods
        self.method = method

    def find(self,haystack_img,threshold=0.85,debug_mode=None):
        #Found the best result  
        result = cv.matchTemplate(haystack_img,self.needle_img,self.method)

        locations = np.where(result >= threshold)

        #Unpack the list and convert them in tuples
        locations = list(zip(*locations[::-1]))

        #we need to create a list of rectangles to group them and not have overlap
        rectangles= []
        for loc in locations:
            rect=[int(loc[0]),int(loc[1]),self.needle_w,self.needle_h]
            rectangles.append(rect)
            rectangles.append(rect) # this secondone is for always is 2 rectangles to group
        rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

        points=[]
        if len(rectangles):
            print("Found")

            #get the dimenssions of the needle imagen

            line_color = (0,255,0)
            lineType=cv.LINE_4
            marker_color = (255,0,255)
            marker_type = cv.MARKER_CROSS
            
            for (x,y,w,h) in rectangles:
                # determine center position
            
                center_x = x+ int(w/2)
                center_y = y+ int(h/6)
                # Save pounts
                points.append((center_x,center_y))

            if debug_mode == "rectangles":
                # Determine the box position
                top_left= (x,y)
                bottom_right=(x + w, y+ h)
                #Draw the box
                cv.rectangle(haystack_img,top_left,bottom_right,line_color,lineType)
            elif debug_mode == "points":
                cv.drawMarker(haystack_img,(center_x,center_y),marker_color,marker_type)

        if debug_mode:
            cv.imshow("Bot",haystack_img)
            #cv.waitKey()
        
        return points
    def draw_rectangles(self, haystack_img, rectangles):
        # these colors are actually BGR
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            # determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, lineType=line_type)

        return haystack_img

    #points= findClickPosition("dummy.png","Main_screen.png",debug_mode="rectangles")