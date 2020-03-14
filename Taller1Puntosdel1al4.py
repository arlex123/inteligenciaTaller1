#RESPUESTA PUNTOs DEL 1 AL 4 DEL TALLER #1 ARLEX SAAVEDRA COD:230171022

import re 
import smtplib
import getpass

correo = input("Digite su correo : ")
contraseña = getpass.getpass("Digite su contraseña: ")

if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower()):
  
    gmail_user = correo
    gmail_password = contraseña
    sender = correo
    receivers = ['arle.x99@outlook.com']
    message = """ From: Arlex Saavedra <saavedraarlex@gmail.com>
    To: Arlex Saavedra <arle.x99@outlook.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        #smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(gmail_user, gmail_password)
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
else:
    print("Correo incorrecto")
