#!/usr/bin/env python3
#Author: Basuh94

import cv2
import matplotlib.pyplot as plt

def ConvertImage():
    print( "Welcome to the program to show the outline of an image. If you want to exit the program, type 'EXIT'" )
    inputImage=input( 'Insert the path of your image to work with it: ' )
    if( inputImage == 'exit' or inputImage == 'EXIT' ):
        print( 'Goodbye!' )
        exit()
    else:
        try:
            image = cv2.imread( inputImage )
            gray_image = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
            rgb_image = cv2.cvtColor( image, cv2.COLOR_BGR2RGB )
            #cv2.imshow("Gray Image" + inputImage, gray_image)
            #cv2.imshow("RGB Image " + inputImage, image)
            BinaryImage( gray_image, rgb_image )
        except:
            print( 'Image path is wrong or does not exist.' )
            return ConvertImage()

def BinaryImage( gray_image, rgb_image ):
    try:
        _,binary = cv2.threshold( gray_image, 225, 255, cv2.THRESH_BINARY )
        plt.imshow( binary, cmap="gray" )
        plt.show()
        ContourImage( binary, rgb_image )
    except:
        print( 'There was an ERROR converting the image to binary.' )
        return ConvertImage()

def ContourImage( binary, rgb_image ):
    try:
        contour,_= cv2.findContours( binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
        image = cv2.drawContours( rgb_image, contour, -1, (0,255,0), 2 )
        plt.imshow( image )
        plt.show()
    except:
        print( 'There was an ERROR performing the image outline.' )
        return ConvertImage()

ConvertImage()        
cv2.waitKey( 0 )
cv2.destroyAllWindows()