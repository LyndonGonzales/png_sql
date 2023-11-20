"""To convert a PNG file to a blob and save it in MSSQL
1. Read the PNG file as binary data.
2. Create a connection to your MSSQL database.
3. Prepare an SQL INSERT statement with a parameter for the blob data.
4. Bind the binary data to the parameter.
5. Execute the SQL statement to insert the blob data into the database.
"""
from helper_functions import *

# Read the PNG file as binary data
with open('264.png', 'rb') as file:
    png_data = file.read()

conn = get_conn_azure()

sql = "INSERT INTO BDS_AARBOT_IMAGES (name,png_data) VALUES (?,?)"

#select name,png_data from BDS_AARBOT_IMAGES
#we dont need binary conversion of this file. leave as-is.
params = ('264_raw',pyodbc.Binary(png_data)) #params = (pyodbc.Binary(png_data),)
cursor = conn.cursor()
cursor.execute(sql, params)
conn.commit()

conn.close()
