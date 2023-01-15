import qrcode

data = input('Paste the url to generate the QR Code: ')

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'pink', back_color = 'white')

img.save('C:/Users/beatr/OneDrive/Área de Trabalho/RockPaperScissor/myqrcode.png')