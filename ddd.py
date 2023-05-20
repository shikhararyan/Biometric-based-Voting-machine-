import requests
import urllib3
import fingerprint
import base64
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



def match_fingerprints(template1, template2):
    matcher = fingerprint.FingerprintMatcher()
    score = matcher.match(template1, template2)
    
    # Adjust the matching threshold as per your requirements
    threshold = 40
    
    if score >= threshold:
        return True
    else:
        return False


# Usage
my_finger_print_base64 = ""

data = get_data_from_http()
if data:
    print("Data retrieved successfully!")
    print("Data:", data)
else:
    print("Failed to retrieve data from HTTP server.")


# Extract the template values from the JSON data
template1 = base64.b64decode(data["TemplateBase64"])
template2 = base64.b64decode(my_finger_print_base64)

# Compare the fingerprints
if match_fingerprints(template1, template2):
    print("Fingerprints match.")
else:
    print("Fingerprints do not match.")