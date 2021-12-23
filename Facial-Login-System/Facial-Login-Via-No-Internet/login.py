import os
import numpy as np
import cv2
import face_recognition

Username = str(input("Enter Your UsernameID : "))
filearray = "array_data/"+Username+".npy"

try:
  dImg = np.load(filearray)
except:
  print("Incorrect UsernameID!")
  exit()

cap = cv2.VideoCapture(0)
while True:
    return_value,image = cap.read()
    cv2.imshow('INPUT - Press S To ScreenShot!',image)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('screenshotimage.jpg',image)
        break

cap.release()
cv2.destroyAllWindows()

os.system("cls")
img = face_recognition.load_image_file("screenshotimage.jpg")
try:
  sImg = face_recognition.face_encodings(img)[0]
except:
  print("Facial Error!\nPlease Use Your Full Face Image Correctly!")
  os.remove("screenshotimage.jpg")
  exit()
os.system("cls")
os.remove("screenshotimage.jpg")
result = face_recognition.compare_faces([dImg], sImg)
os.system("cls")
if str(result) == "[True]":
   print("WELCOME USER!")
else:
     print("UNKNOWN PERSON DETECTED!")