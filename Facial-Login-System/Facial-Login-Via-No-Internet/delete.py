import os

value = str(input("Please Enter Your UsernameID To Delete Your Account : "))
answer = value + ".npy"

try:
  os.remove("array_data/"+answer)
except:
  print("Your Account [ID="+value+"] Doesnt Even Exist!")
  exit()

print("Your Account [ID="+value+"] Has Been Successfully Deleted!")