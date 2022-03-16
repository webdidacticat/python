# -*- coding: utf-8 -*-

####
#### Necesario tener instalado en el PC el servicio SMTP
#### 

import smtplib

def email():
        ### Codi per enviar un mail
        from_addr = 'mail_username@gmail.com'
        to = 'mail_desino@gmail.com'
        subject = 'Subject: E-mail HTML enviado desde Python\n'
        message = subject + """Hola!<br/> <br/>Este es un <b>e-mail</b> enviand$

        # Reemplaza estos valores con tus credenciales de Google Mail
        username = 'mail_username@gmail.com'
        password = 'password'

        try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                server.login(username, password)
                server.sendmail(from_addr, to, message)
                print("Correo enviado")
        except:
                print("Error: el mensaje no pudo enviarse.\nCompruebe que sendmail se encuentra instalado en su sistema")

        server.quit()

email()

