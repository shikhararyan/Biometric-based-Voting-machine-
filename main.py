import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def verify_aadhar():
    aadhar_number = entry.get()

    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Shikhar@12',
            database='voters'
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Check if the Aadhar number exists in the voters1 table
        query = "SELECT * FROM voters1 WHERE aadhar = %s"
        cursor.execute(query, (aadhar_number,))
        voter_result = cursor.fetchone()

        if voter_result:
            # Check if the Aadhar number exists in the votes table
            query = "SELECT * FROM votes WHERE aadhar = %s"
            cursor.execute(query, (aadhar_number,))
            vote_result = cursor.fetchone()

            if vote_result:
                messagebox.showinfo("Vote Status", "Vote already casted.")
            else:
                messagebox.showinfo("Vote Status", "Voter ID exists. Calling finger.py module...")
                # Call your finger.py module or function here

        else:
            messagebox.showinfo("Vote Status", "Voter ID does not exist.")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        messagebox.showerror("MySQL Error", f"Error connecting to MySQL: {error}")

# Create a Tkinter window
window = tk.Tk()
window.title("Voting Machine")
window.geometry("800x800")

background_image = Image.open("C:\\Users\\shikh\\OneDrive\\Desktop\\hiluuu\\logo\\background.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create small icons on the top right corner
icon1 = tk.PhotoImage(file="C:\\Users\\shikh\\OneDrive\\Desktop\\hiluuu\\logo\\eci_logo.png").subsample(5, 5)
icon2 = tk.PhotoImage(file="C:\\Users\\shikh\\OneDrive\\Desktop\\hiluuu\\logo\\Adhaar-Logo.png").subsample(19, 19)

icon_label1 = tk.Label(window, image=icon1)
icon_label1.place(x=100, y=10)

icon_label2 = tk.Label(window, image=icon2)
icon_label2.place(x=180, y=10)



# Create a label and an entry field for Aadhar number
label = tk.Label(window, text="Enter Aadhar Card Number:", font=("Arial", 12))
label.place(relx=0.5, rely=0.3, anchor="center")

entry = tk.Entry(window, font=("Arial", 12))
entry.place(relx=0.5, rely=0.4, anchor="center")

# Create a button to verify Aadhar number
button = tk.Button(window, text="Verify", command=verify_aadhar, font=("Arial", 12))
button.place(relx=0.5, rely=0.5, anchor="center")

# Start the Tkinter event loop
window.mainloop()
