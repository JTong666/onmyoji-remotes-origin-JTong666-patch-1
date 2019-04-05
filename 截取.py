
import cv2


image = cv2.imread("JT3.jpg")
image2 = image[547: 569, 603:660, :]
cv2.imwrite("end_yue.png", image2)
cv2.imshow("iamge-1", image2)
cv2.waitKey(0)

