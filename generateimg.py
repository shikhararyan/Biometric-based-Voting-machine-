import requests
import urllib3
import base64
from PIL import Image
from io import BytesIO

def get_data_from_http():
    url = "https://localhost:8000/SGIFPCapture"  # Replace with the actual URL of your local HTTP server

    try:
        # Disable SSL certificate verification
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        response = requests.get(url, verify=False)  # Disable certificate verification

        response.raise_for_status()  # Raise an exception for any HTTP error status codes

        data = response.json()  # Assuming the response is in JSON format

        return data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

for i in range(100):
    data = get_data_from_http()
    if data:
        print("Data retrieved successfully!")
        print("Data Keys",data.keys())

        # Decode the BMPBase64 string
        bmp_data = base64.b64decode(data["BMPBase64"])

        # Create an in-memory stream for the image data
        stream = BytesIO(bmp_data)

        # Open the stream as an image using PIL
        image = Image.open(stream)

        # Save the image to a file
        image.save("real/output_{0}.bmp".format(i))  # Provide the desired filename with appropriate extension
    else:
        print("Failed to retrieve data from HTTP server.")