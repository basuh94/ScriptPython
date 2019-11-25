import cv2
import matplotlib.pyplot as plt 

inputImage=input('Insert the path of your image to work with it: ')
image = cv2.imread(inputImage)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

_,binaria = cv2.threshold(gray_image, 225, 255, cv2.THRESH_BINARY)
plt.imshow(binaria, cmap="gray")
plt.show()

contornos,_= cv2.findContours(binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(rgb_image, contornos, -1, (0,255,0),2 )
#cv2.imshow("Gray Image", gray_image)
#cv2.imshow("Contour " + inputImage, image)
plt.imshow(image)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()