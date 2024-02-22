from django.core.mail import send_mail
from django.conf import settings

def send_password_reset_email():
    
    # Enviar e-mail
    subject = 'Redefinir senha'
    message = 'Obrigado por estar aqui!'

    send_mail(subject, 
              message, 
              settings.EMAIL_HOST_USER, 
              ['victorcaua03@gmail.com'])
