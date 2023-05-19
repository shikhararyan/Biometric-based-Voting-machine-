import pysgfplib
import secugenfdx
from secugenfdx import SGFDxDeviceName, SGFingerPrintManager

# Initialize the fingerprint scanner
device_name = SGFDxDeviceName.DEV_AUTO
finger_print_manager = SGFingerPrintManager()
finger_print_manager.Init(device_name)

# Capture the fingerprint image
finger_print_manager.OpenDevice()
finger_print_manager.SetTemplateFormat(secugenfdx.ANSI378)
finger_print_manager.Capture()

# Extract the fingerprint features
finger_print_manager.CreateTemplate()

# Get the binary template
binary_template = finger_print_manager.GetTemplate()

# Close the fingerprint scanner device
finger_print_manager.CloseDevice()

# Now you have the binary template, you can use it for database comparison or other purposes
