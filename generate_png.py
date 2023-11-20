from helper_functions import *

conn = get_conn_azure()
cursor = conn.cursor()

query = "SELECT png_data FROM BDS_AARBOT_IMAGES WHERE name = '264_raw' "
# Replace <condition> with the appropriate condition to retrieve the desired record(s)

# Execute the SQL query
cursor.execute(query)

# Fetch the result
result = cursor.fetchone()

# Get the binary data from the result
binary_data = result.png_data

with open('test.png', 'wb') as file:
	file.write(binary_data)
	file.close()

# Close the database connection
cursor.close()
conn.close()

