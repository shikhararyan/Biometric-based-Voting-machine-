import requests
import urllib3
import base64
from PIL import Image
from io import BytesIO

def getFP(folder_path,file_name):
    url = "https://localhost:8000/SGIFPCapture"  # Replace with the actual URL of your local HTTP server

    try:
        # Disable SSL certificate verification
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        response = requests.get(url, verify=False)  # Disable certificate verification

        response.raise_for_status()  # Raise an exception for any HTTP error status codes

        data = response.json()  # Assuming the response is in JSON format

        # Decode the BMPBase64 string
        bmp_data = base64.b64decode(data["BMPBase64"])
        print(bmp_data)

        # Create an in-memory stream for the image data
        stream = BytesIO(bmp_data)

        # Open the stream as an image using PIL
        image = Image.open(stream)

        # Save the image to a file
        image.save("{0}/{1}.bmp".format(folder_path,file_name))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    
