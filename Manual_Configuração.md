# Instruções da configuração da raspberry

## Configurações iniciais da raspberry

### Pinagem da placa:

![alt text](https://github.com/matheuscivusp/Modulo_rasp/blob/main/Raspberry-Pi-3-model-B-module-and-pin-out.png)

Baixar o Sistema Operacional, Raspberry Pi OS [Link Text](https://www.raspberrypi.com/software/),[[https://www.raspberrypi.com/software/] e gravar o sistema no cartão SD, configurando o usuário e senha como quiser, mas lembrar de habilitar a conexão SSH.

Todas as raspberry estão utilizando o nome e senha padrão

Consertar o horário da raspberry

Atualizações padrões da rasp

$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get autoremove

## Configurando a câmera webcam

É necessário configurar a raspberry para reconhecer a câmera USB e habilitar suas funcionalidades.

Para isso, no terminal:

$ sudo raspi-config

Agora é necessário ir em "3 Interface option" e selecionar a opção "câmera" para desativá-la. (Isso desativa o conector CSI da câmera modular da raspberry)

O seguinte comando irá listar os dispositivos conectados às portas USBs.

$ lsusb

A câmera deve aparecer

Agora, é necessário insalar um pacote para interagir com a webcam:

$ sudo apt install fswebcam

$ sudo usermod -a -G video gabriel

$ groups

reboot

Agora é necessário criar um script (arquivo .sh) linux que irá tirar as fotos e salvar no formato que queremos:

Pegar na raspberry

Tornar o .sh um arquivo executável

Também criamos um programa em Python para tirar essas fotos usando um botão:

- código no git




## Desenvolvimento do botão de boot

Inicializando e desligando a raspberry por um push button

A raspberry não ligará quando for conectada à energia, apenas quando o botão for pressionado, um LED permanecerá ligado enquanto a raspberry estiver ativa.

Pressionando o botão novamente a rasp vai desligar e o LED irá apagar.

Instalando bibliotecas padrões pelo terminal:

$ sudo apt-get update

$ sudo apt-get install python-dev python-rpi.gpio

Criar um script em Python que detecte quando o botão é pressionado

- Código salvo no Git

Make the script executable by running the following command:

$ chmod +x wait_for_button.py

Para executar o código no terminal:

$ python <nome>.py
    
Agora é necessário editar um arquivo de boot da raspberry, pelo terminal, digite:

$ sudo nano /boot/config.txt
    
    Adicione o seguinte comando no final do arquivo:
    
$ dtoverlay=gpio-shutdown,gpio_pin=17,active_low=1,gpio_pull=up
    
    Save the file by pressing Ctrl+X, then Y, and then Enter.
    
    
### Colocando o código para rodar no boot:
    
Edit the rc.local file to run the script at startup. Run the following command:

$ sudo nano /etc/rc.local

Add the following line before the exit 0 line:

$ /home/pi/wait_for_button.py &

This line runs the wait_for_button.py script in the background at startup.

Save the file by pressing Ctrl+X, then Y, and then Enter.

Reboot your Raspberry Pi by running the following command:

$ sudo reboot
    
    O processo está finalizado

## Desenvolvimento do botão para tirar fotos e slavar na pasta de upload
## Desenvolvimento da comunicação e envio dos arquivos para o drive

# Modulo_rasp - Histórico de projeto 
Repositório dedicado à construção dos módulos de imagens do IMA-MT, utilizando raspberry e webcam
Manual de construção e configuração

## Upload Drive

Preparar drive para upload automático das imagens tiradas pelo módulo da rasp

### Resposta do ChatGPT

There are several ways to upload files from a Raspberry Pi to a Google Drive folder, but one common method is to use the Google Drive API and a programming language such as Python. Here are the basic steps:

1. Set up a Google Cloud Platform project and enable the Google Drive API for it. You will need to create credentials (client ID and secret) to authenticate your application.

2. Install the Google API client library for Python on your Raspberry Pi.

3. Write a Python script that uses the Google Drive API to authorize your application, create a new folder in your Google Drive, and upload the files from the local folder to the Google Drive folder. Here's a sample code that you can modify to fit your needs:

## ==================== Código =============================

import os

from google.oauth2.credentials import Credentials

from googleapiclient.discovery import build

from googleapiclient.errors import HttpError

from googleapiclient.http import MediaFileUpload

Comentário python # Define the path to the local folder and the ID of the Google Drive folder

local_folder = '/path/to/local/folder'

drive_folder_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

Comentário python # Define the credentials object

creds = Credentials.from_authorized_user_file('/path/to/credentials.json')

Comentário python # Create a new Drive API client

drive_service = build('drive', 'v3', credentials=creds)

Comentário python # Create a new folder in the Google Drive

folder_metadata = {'name': 'My Folder', 'parents': [drive_folder_id], 'mimeType': 'application/vnd.google-apps.folder'}

folder = drive_service.files().create(body=folder_metadata, fields='id').execute()

Comentário python # Upload the files to the Google Drive folder

for filename in os.listdir(local_folder):

    file_metadata = {'name': filename, 'parents': [folder['id']]}
    
    media = MediaFileUpload(os.path.join(local_folder, filename), resumable=True)
    
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    
## ====================================================================================
4. Save the script as a Python file and run it on your Raspberry Pi using a cron job or a similar scheduling tool to automate the upload process.

Note that this is just a basic example, and you may need to modify the code to handle errors, upload large files, or customize the folder structure. You can find more information about the Google Drive API and how to use it with Python in the official documentation.


## Desenvolvimento da execução dos códigos e scripts no boot
## Hardware
## Construção da Case
## Elaboração de testes
## Utilização do Ansible
