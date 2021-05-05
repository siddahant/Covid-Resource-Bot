import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd

def res1():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("ICBOT2021").worksheet('Sheet1') # Open the spreadhseet

    data = sheet.get_all_records()  # Get a list of all records

    df = pd.DataFrame(data)
    update1 = df.drop_duplicates(subset=['resource'])

    update = update1["resource"].tolist()



    return update
