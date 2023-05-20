import os
from secugen import getFP
name = input("Enter your name:")
aadhar = input("Enter your aadhar:")
phone = input("Enter your phone number:")

folder_path = os.path.join(os.getcwd(), aadhar)

# Create the folder
os.makedirs(folder_path)

print(f"Folder '{aadhar}' created at '{folder_path}' for the citizen of india - '{name}'.")

# capture 5 fingerprint for new citizen

for i in range(5):
    print('scan your fingerprint when device turns green.')
    getFP(folder_path,aadhar+"_"+i)
    print("{0}-th scan has been completed.".format(i+1))



