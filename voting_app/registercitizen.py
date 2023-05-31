import os
from secugen import getFP
name = input("Enter your name:")
aadhar = input("Enter your aadhar:")
age = input("Enter your age:")
folder_path = os.path.join(os.getcwd(), aadhar)


# Create the folders
os.makedirs(aadhar)

print(f"Folder '{aadhar}' created at '{aadhar}' for the citizen of india - '{name}'.")

# capture 5 fingerprint for new citizenshikhar

for i in range(5):
    print('scan your fingerprint when device turns green.')
    getFP(aadhar,aadhar+"_"+ str(i))
    print("{0}-th scan has been completed.".format(i+1))



