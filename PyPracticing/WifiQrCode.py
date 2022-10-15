import wifi_qrcode_generator

ssid = input('Nome da rede: ')
password = input('Senha da rede: ')
type = 'WPA'

img = wifi_qrcode_generator.wifi_qrcode(ssid, False, type, password)
img.save(ssid+'.png')
