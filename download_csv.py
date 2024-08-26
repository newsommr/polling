import requests

# URL of the Google Sheets CSV
csv_url = "https://docs.google.com/spreadsheets/d/1d95yYYoLsrSR-RlPs-kPWkzksGkBaFAJrdnQ4sQiO58/export?format=csv&id=1d95yYYoLsrSR-RlPs-kPWkzksGkBaFAJrdnQ4sQiO58&gid=684601453"

# Path to save the CSV locally
local_filename = "latest_data.csv"

# Download the CSV
response = requests.get(csv_url)

# Save the CSV file
with open(local_filename, 'wb') as file:
    file.write(response.content)

print(f"CSV file downloaded and saved as {local_filename}.")
