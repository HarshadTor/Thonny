import gspread
import time
import numpy as np
from google.oauth2.service_account import Credentials

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", 
          "https://www.googleapis.com/auth/drive"]

# Load credentials
creds = Credentials.from_service_account_file("key.json", scopes=SCOPES)

# Connect to Google Sheets
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Untitled spreadsheet").sheet1  
def update_column():
    row = 1  
    while True:
        random_number = np.random.randint(1, 100)  
        sheet.update(f"A{row}", [[random_number]])  
        print(f"Updated A{row} with {random_number}")
        
        row += 1  
        if row > 100:  
            row = 1

# Run the function
update_column()
