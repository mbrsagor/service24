import uuid
from django.core.mail import send_mail


def send_forgot_password_mail(email):
    token = str(uuid.uuid4())
    subject = 'Your forgot password link'
    message = f"Hi, click on the link to forgot your password http://127.0.0.1:8000/forgot-password/{token}/"
