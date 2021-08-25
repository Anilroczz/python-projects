import cv2

temp = cv2.QRCodeDetector()
val,_,_ = temp.detectAndDecode(cv2.imread("youtubeQR.jpg"))
print("Encoded Text : "+val)