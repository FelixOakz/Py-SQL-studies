import wifi_qrcode_generator

ssid = input('Home wifi')
type = 'WPA'
password = input('very complicated password')

img = wifi_qrcode_generator.wifi_qrcode(ssid, False, type , password)
img.save(ssid+'.png')