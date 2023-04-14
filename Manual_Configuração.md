# Instruções da configuração da raspberry

## Instalando funções básicas da raspberry

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

Agora, é necessário insalar um pacote para interagir com a webcam



## Desenvolvimento do botão de boot
## Desenvolvimento do botão para tirar fotos e slavar na pasta de upload
## Desenvolvimento da comunicação e envio dos arquivos para o drive
## Desenvolvimento da execução dos códigos e scripts no boot
## Hardware
## Construção da Case
## Elaboração de testes
## Utilização do Ansible
