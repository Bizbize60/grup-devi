# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:57:14 2023

@author: BBS
"""

import cv2
import numpy as np 

class Person:
    def __init__(self,name):
        self.name=name





class MenuDetector:
    def __init__(self,Object,imageurl):
        self.imageurl=imageurl
        self.Object=Object
        
        self.detectcolor()
    def detectcolor(self):
        self.image = cv2.imread(self.imageurl, cv2.IMREAD_COLOR)
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
       
        
        self.red_lower = np.array([160, 50, 50], np.uint8) 
        self.red_upper = np.array([180, 255, 255], np.uint8) 
        self.red_mask = cv2.inRange(self.hsv, self.red_lower, self.red_upper) 
        
        
        
        self.green_lower = np.array([35, 100,100]) 
        self.green_upper = np.array([75, 255, 255]) 
        self.green_mask = cv2.inRange(self.hsv, self.green_lower, self.green_upper) 
        
        

        
        self.blue_lower = np.array([75, 100, 100], np.uint8) 
        self.blue_upper = np.array([130, 255, 255], np.uint8) 
        self.blue_mask = cv2.inRange(self.hsv, self.blue_lower, self.blue_upper)
        
        
        
        self.contourred,hiearchy=cv2.findContours(self.red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contourgreen,hiearchy=cv2.findContours(self.green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contourblue,hiearchy=cv2.findContours(self.blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        

        cv2.imshow("frame",self.green_mask)
        cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
        cv2.destroyAllWindows()
       
        
        self.counter=0
        self.color="x"
        for i in range(len(self.contourred)):
           
            
                
                if cv2.contourArea(self.contourred[i]) > 1000: 
                    self.contour=self.contourred[0]
                    self.color="red"
                   
                    self.detectshape()
          
        for i in range(len(self.contourgreen)):
                if cv2.contourArea(self.contourgreen[i])>1000:
                    self.contour=self.contourgreen[0]
                    self.color="green"
                    self.detectshape()
           
        for i in range(len(self.contourblue)):
              if cv2.contourArea(self.contourblue[i])>1000:
                    self.contour=self.contourblue[0]
                    self.color="blue"
                 
                    self.detectshape()
           
    def detectshape(self):
        self.counter+=1
        self.shape="x"
        self.peri=cv2.arcLength(self.contour,True)
        self.approx=cv2.approxPolyDP(self.contour, 0.04*self.peri, True)
        if self.counter==1:
            if len(self.approx)==3:
                self.shape="triangle"
                    
            elif len(self.approx)==4:
                self.shape="rectangle"
            else:
                self.shape="circle"
                
            #Buradaki self.shape self.color ve self.objecti kullanıp yukardaki person classına git ve hesaplamaları yap
            print(self.shape,self.color)
        else:
            pass
        
                

ahmet=Person("ahmet")
yemek1=MenuDetector(ahmet,"C:/Users/BBS/Desktop/greenrectangle.png")        