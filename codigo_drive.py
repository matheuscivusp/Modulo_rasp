import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define o caminho para a pasta local e o ID da pasta compartilhada no Google Drive
pasta_local = '/caminho/para/pasta/local'
drive_pasta_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Define as credenciais
creds = Credentials.from_authorized_user_file('/caminho/para/credentials.json')

# Cria um cliente da API do Google Drive
drive_service = build('drive', 'v3', credentials=creds)

# Faz o upload das imagens para a pasta compartilhada
for nome_arquivo in os.listdir(pasta_local):
    arquivo_metadata = {'name': nome_arquivo, 'parents': [drive_pasta_id]}
    media = MediaFileUpload(os.path.join(pasta_local, nome_arquivo), resumable=True)
    arquivo = drive_service.files().create(body=arquivo_metadata, media_body=media, fields='id').execute()
    
# Obtém informações da pasta compartilhada
shared_folder = drive_service.files().get(fileId=drive_pasta_id, fields='id, name, permissions').execute()

# Imprime o ID, nome e permissões da pasta compartilhada
print("ID da pasta compartilhada:", shared_folder['id'])
print("Nome da pasta compartilhada:", shared_folder['name'])
print("Permissões da pasta compartilhada:")
for permission in shared_folder['permissions']:
    print(" - Email: ", permission['emailAddress'])
    print("   Tipo: ", permission['type'])
    print("   Papel: ", permission['role'])

