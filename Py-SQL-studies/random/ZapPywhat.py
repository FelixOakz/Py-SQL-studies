import pywhatkit as zap

ent = str(input('Numero: '))
num = '+5584'+ent

msg = str(input('Msg a ser enviada: '))

hr = int(input('Hora: '))
min = int(input('Min: '))

zap.sendwhatmsg(num, msg, hr, min)
