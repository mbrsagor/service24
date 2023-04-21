import uuid
from django.core.mail import send_mail
from django.conf import settings

def send_forgot_password_mail(email):
    token = str(uuid.uuid4())
    subject = 'Your forgot password link'
    message = f"Hi, click on the link to forgot your password {settings.HOST_URL}forgot-password/{token}/"
