import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Define the path to the local folder and the ID of the Google Drive folder
local_folder = '/path/to/local/folder'
drive_folder_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Define the credentials object
creds = Credentials.from_authorized_user_file('/path/to/credentials.json')

# Create a new Drive API client
drive_service = build('drive', 'v3', credentials=creds)

# Create a new folder in the Google Drive
folder_metadata = {'name': 'My Folder', 'parents': [drive_folder_id], 'mimeType': 'application/vnd.google-apps.folder'}
folder = drive_service.files().create(body=folder_metadata, fields='id').execute()

# Upload the files to the Google Drive folder
for filename in os.listdir(local_folder):
    file_metadata = {'name': filename, 'parents': [folder['id']]}
    media = MediaFileUpload(os.path.join(local_folder, filename), resumable=True)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
