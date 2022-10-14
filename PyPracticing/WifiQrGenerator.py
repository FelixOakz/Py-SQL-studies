import qrcode

network = input('Enter your network name: ')
password = input('Enter your passsword: ')

qrcode = qrcode.QRCode()
qrcode.add_data(f'{network} {password}')
qrcode.make_image().save('WifiQR.png')

