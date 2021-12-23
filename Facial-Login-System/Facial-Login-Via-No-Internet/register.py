import os
import uuid
import numpy as np
import cv2
import face_recognition

id_name = str(uuid.uuid4().hex[:8])
id_fullname = id_name+".jpg"
numpyfile = "array_data/"+id_name

cap = cv2.VideoCapture(0)
while True:
    return_value,image = cap.read()
    cv2.imshow('INPUT - Press S To ScreenShot!',image)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite(id_fullname,image)
        break
cap.release()
cv2.destroyAllWindows()


#CHECKING WHETHER PROFILE EXIST OR NOT
for filename in os.listdir("array_data/"):
    if filename.endswith(".npy"):
         abc = face_recognition.load_image_file(id_fullname)
         try:
           valueOne = face_recognition.face_encodings(abc)[0]
         except:
           os.system("cls")
           print("Facial Error!\nPlease Use Your Full Face Image Correctly!")
           os.remove(id_fullname)
           exit()
         valueTwo = np.load("array_data/"+filename)
         result = face_recognition.compare_faces([valueOne], valueTwo)
         os.system("cls")
         if str(result) == "[True]":
            print("You Are Already A Registered User WIth UsernameID - "+filename[0:len(filename)-4])
            os.remove(id_fullname)
            quit()
         else:
              print("Loading......")


img = face_recognition.load_image_file(id_fullname)
try:
  result = face_recognition.face_encodings(img)[0]
except:
  os.system("cls")
  print("Facial Error!\nPlease Use Your Full Face Image Correctly!")
  os.remove(id_fullname);
  exit()

os.remove(id_fullname);
np.save(numpyfile, result)
os.system("cls")
print("Welcome To Mushahid Ali Solutions!\nThere Are Currently "+str(len(os.listdir(os.getcwd()+"\\array_data")))+" Users Registered Including You!\nCONGRATULATIONS!")
print("\nYour Registered UsernameID Is : "+id_name)