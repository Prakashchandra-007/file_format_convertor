
import convertapi
import os
import tempfile
import requests
from io import FileIO
import sys

file_path = 'files/test1.docx'


secret = 'b5bFnMARf9kEpth0'
convertapi.api_secret = 'b5bFnMARf9kEpth0'  # your api secret
url = 'https://v2.convertapi.com/docx/to/pdf?secret=' + secret
files = {'file': open(file_path, 'rb')}
headers = {'Accept': 'application/octet-stream'}
response = requests.post(url, files=files, headers=headers)
print(response)
if response.status_code != 200:
    sys.exit(response.text)
# Example of saving Word docx to PDF and to PNG
# https://www.convertapi.com/docx-to-pdf
# https://www.convertapi.com/docx-to-png

# Use upload IO wrapper to upload file only once to the API
# print()
# upload_io = convertapi.UploadIO(open('files/test1.docx', 'rb'))
# print(upload_io)

# saved_files = convertapi.convert(
#     'pdf', {'File': upload_io}).save_files(tempfile.gettempdir())

# print("The PDF saved to %s" % saved_files)

# # Reuse the same uploaded file

# saved_files = convertapi.convert(
#     'png', {'File': upload_io}).save_files(tempfile.gettempdir())

# print("The PNG saved to %s" % saved_files)
