# Manual de uso do Módulo

## Descrição do Hardware
O módulo é composto por:

- 1 Raspberry pi 3 model B (adcionar imagem?)
- 1 Power Bank (modelo...)
- 2 Leds
- 2 Botões
- 1 Case

## Funcionamento resumido
  Com o power bank estando com carga, basta apertar o botão que se encontra quase no meio do módulo (o mais próximo da câmera) para ligar a raspberry, um led indicará que a raspberry está ligada e funcionando, esperar até que o led esteja estável. O mesmo botão é utilizado para desligar, desligando a raspberry o Led também se apagará. Esperar alguns segundos quando for desligar a raspberry para que todos os arquivos sejam salvos com sucesso e o desligamento ocorra normalmente, e ao ligar também aguardar alguns segundos (60 segundos aproximadamente) para a raspberry inicializar todas as suas configurações até começar a tirar as fotos.

  O outro botão é o responsável por tirar as fotos, um led irá piscar quando a foto for tirada, a webcam também possui um led próprio (ao redor da lente) que indica que a foto foi tirada. Portanto, basta apontar a lente da câmera para o objeto a ser capturado e pressionar o botão que está mais próximo da extremidade do módulo, aguardar aproximadamente 2 segundos até que o led acenda por 1 segundo indicando que a imagem foi tirada e salva, após isso é possível tirar outra foto.
  
  Todas as imagens são salvas dentro do armazenamento interno da raspberry no diretório: /pi/Doucuments/imagens, só será possível visualizar as imagens ao acessar a raspberry, o que pode ser feito remotamente através de softwares como o VNC Viewer ou AnyDesk, ou conectando os periféricos (Monitor-HDMI, Mouse-USB, Teclado-USB) nas entradas da raspberry, sendo esse segundo método mais simples e recomendado.


