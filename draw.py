import cv2 as cv
import numpy as np

#to create blank image
blank=np.zeros((500,500,3),dtype='uint8') #(500,500,3)=>(height,width,no. of color channel)
cv.imshow('blank',blank)

blank[:]=0,0,255 #change color of all pixels to red
cv.imshow('new1',blank)
blank[200:300, 300:400]=0,255,0 #change color of pixels range to green
cv.imshow('new2',blank)
#to draw rectange
cv.rectangle(blank, (0,0), (250,250), (0,255,100), thickness=1) #thickness=-1 fill the rectangle with the color, (blank, (0,0), (250,250), (0,255,0), thickness=2)=>(image_name,starting cordinate,ending cordinate,color,thickness of border)
cv.imshow('rect',blank)
cv.rectangle(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2), (0,255,100), thickness=1) #it is the center and the starting cordinate
cv.imshow('new_rect',blank)
#to draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 100,(124,255,200), thickness=1) # 100 is circle radius
cv.imshow('circle',blank)
#to draw line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=2)
cv.imshow('line',blank)
#to write text
cv.putText(blank,'hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)#=>cv.FONT_HERSHEY_TRIPEX=>font style
cv.imshow('text',blank)
cv.waitKey(0) #if we did not put wait key image come and go so wait key 0 means it stay for infinity time
