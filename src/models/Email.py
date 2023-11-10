
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import HTTPException




class Email:

    def __init__(self, smtp_server, smtp_port, smtp_username, smtp_password):
            self.smtp_server = smtp_server
            self.smtp_port = smtp_port
            self.smtp_username = smtp_username
            self.smtp_password = smtp_password

    def send_email(self, to_email, subject, message):
        # Configura el mensaje de correo
        msg = MIMEMultipart()
        msg["From"] = self.smtp_username
        msg["To"] = to_email
        msg["Subject"] = subject

        # Agrega el cuerpo del mensaje
        msg.attach(MIMEText(message, "plain"))

        try:
            # Inicia la conexión SMTP
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Inicia la sesión SMTP
                server.starttls()

                # Inicia sesión con las credenciales
                server.login(self.smtp_username, self.smtp_password)

                # Envía el correo
                

            return {"message": "Email sent successfully"}

        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=f"Error sending email: {str(e)}")