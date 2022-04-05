# -*- coding: utf-8 -*-

####
#### Necesario tener instalado en el PC el servicio SMTP
#### 
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib

def email():
        # create message object instance
        msg = MIMEMultipart()
        ### Codi per enviar un mail
        msg['From'] = 'mail_username@gmail.com'
        msg['To'] = 'mail_desino@gmail.com'
        msg['Subject'] = 'E-mail HTML enviado desde Python'
        message = 'Hola!<br/> <br/>Este es un <b>e-mail</b> enviado con Python'
        msg.attach(MIMEText(message, 'plain')) ## Para enviar solo texto
        msg.attach(MIMEImage(file("google.jpg").read())) ## Para enviar fichero adjunto
        # Reemplaza estos valores con tus credenciales de Google Mail
        password = 'password'

        try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(msg['From'], password)
                server.sendmail(msg['From'],  msg['To'], msg.as_string())
                print("Correo enviado")
        except:
                print("Error: el mensaje no pudo enviarse.\nCompruebe que sendmail se encuentra instalado en su sistema")

        server.quit()

email()

