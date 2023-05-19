import sys
from pyfingerprint.pyfingerprint import PyFingerprint
import mysql.connector

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Shikhar@12',
    'host': 'localhost',
    'database': 'voters',
}

# Initialize the fingerprint scanner
try:
    f = PyFingerprint('Port_#0001.Hub_#0001', 57600, 0xFFFFFFFF, 0x00000000)
    if not f.verifyPassword():
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('Exception: ' + str(e))
    sys.exit(1)

# Connect to the database
try:
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
except mysql.connector.Error as err:
    print('Database connection error: {}'.format(err))
    sys.exit(1)

# Function to capture a fingerprint
def capture_fingerprint():
    print('Waiting for finger...')

    # Wait for finger to be placed on the sensor
    while not f.readImage():
        pass

    # Convert the image to characterics and store it temporarily
    f.convertImage(0x01)
    characteristics = f.downloadCharacteristics()

    # Search the database for a matching fingerprint
    query = 'SELECT id FROM fingerprints'
    cursor.execute(query)
    fingerprints = cursor.fetchall()

    match_found = False
    for fingerprint in fingerprints:
        stored_template = f.loadTemplate(fingerprint[0])
        if f.compareCharacteristics(characteristics, stored_template) == 0:
            match_found = True
            break

    if match_found:
        print('Fingerprint matched!')
    else:
        print('Fingerprint not found!')

# Call the capture fingerprint function
capture_fingerprint()

# Close the database connection
db.close()
