import turtle
import cv2
import numpy as np
import sys
# load image
image_path = "ganesh.jpg"
img = cv2.imread(image_path)

if img is None:
    print(f"error: could not load'{image_path}'.")
    print("check the file name and path.")
    sys.exit()
    
    
    #2. resize image
    target_width = 650
    h, w =img.shape[:2]
    
    target_height = int((h/ w) * target_width)
    img_resized = cv2.resize(img,(target_width,target_height),
                             Indentation=cv2.INTER_ARE)
    ##. create binary image
    _, thresh = cv2.threshold(
        gray,
        70,
        255,
        cv2.THRESH_BINARY
    )
    
    #5. FIND CONTOURS
    contours, hierarchy =
    cv2.findcontours(
        thresh,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_NONE
    )
    
    #6. SETUP TRUTLE CNVEAS
    screen = turtle.Screen()
    screen.setup(
        width=850,
        height=850
        
        
    )
    
    screen.bgcolor("#181B22")
    
    screen.title(
        "Ganesha Matallic Gold Claen Animation"
    )
    
    #6. create turtle pen
    
    pen = turtle.turtle()
    
    pen.hidenturtle()
    
    pen.speed(0)
    
    pen.pensize(1.5)
    
    #7. colours
    
    gold_stroke = "#D49B24"
    
    gold_fill = "#F5C842"
    
    #8. image offset
    
    offset_x = target_width / 2
    offset_y = target_height / 2
    
    #8. convert opencv point to turtle point
    
    def convert_point(point):
        """
        OpenCV coordinates:
        (0,0) = top-left
        
        trutle coordinates:
            (0,0) = center   
        """
         
        x = point[0][0]
        y = point[0][1]
        
        
        turtle_x = x - offset_x
        turtle_y = offset_y - y
        
        return turtle_x, turtle_y - y
    
    #9.draw one contour
    
    def draw_contour(contour):

    if len(contour) < 2:
        return

    first_x, first_y = convert_point(contour[0])

    pen.penup()

    pen.goto(first_x, first_y)

    pen.pendown()

    for point in contour[1:]:

        x, y = convert_point(point)

        pen.goto(x, y)

    pen.penup()
    
    #10. sort contours by size
    
    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
        
    )
    
    #11.draw ganesha
    
    print("Strarting Ganesha animation...")
    for contour in contours:
        area = 
      cv2.contourArea(contour)
      
          if area < 10:
              continue
          pen.color(gold_stroke)
          
          draw_contour(contour)
          
          #12.add center 
          
          pen.color(gold_fill)
          
          pen.pensize(2)
          
          #13. finish
          
          print("Ganesha drawing completed!")
          
          screen.mainloop()  