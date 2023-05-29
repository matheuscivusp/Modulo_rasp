# Instruções da configuração da raspberry

## Configurações iniciais da raspberry

### Pinagem da placa:

![alt text](https://github.com/matheuscivusp/Modulo_rasp/blob/main/Raspberry-Pi-3-model-B-module-and-pin-out.png)

Baixar o Sistema Operacional, Raspberry Pi OS [https://www.raspberrypi.com/software/], e gravar o sistema no cartão SD, configurando o usuário e senha como quiser, mas lembrar de habilitar a conexão SSH.

Todas as raspberry estão utilizando o nome e senha padrão. (Usuário: pi, Senha: raspberry)

Consertar o horário da raspberry, normalmente o horário só é atualizado quando conectado à rede, testar: 
$ sudo cp /usr/share/zoneinfo/right/America/Sao_Paulo /boot/LOCALTIME

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

## Desenvolvimento da execução dos códigos e scripts no boot
## Hardware
## Construção da Case
    
    Uma case foi desenvolvida na plataforma onshape (CAD) para armazenar todo o sistema embarcado
    
    Inserir a imagem da case aqui:
    
    #Detalhes da motagem:
    
    A case possui uma tampa que é encaixada mecanicamente para permitir uma fácil manutenção dos componentes. A imagem já descreve
    bem a montagem, botões e led para fora da caixa através dos buracos e as entradas e saídas da powerbank e rasp abertas para
    permitir as conexões, a câmera fica projetada e encaixada mecanicamente, alguns componentes são fixados mecanicamente
    
    
    
## Elaboração de testes
    
    Descrever todos os testes no manual de usuário
    
    Testes a serem realizados: tempo de autonomia da bateria (20.000 mAh)
    Teste com a conectividade: testar apenas colocando no cabo de rede ethernet, ver se ocorre o upload das imagens
    
## Utilização do Ansible
