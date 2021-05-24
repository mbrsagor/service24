from django.core.mail import EmailMessage
from django.conf import settings
from logs.log import Log


class NotificationEmailService:
    def __init__(self, request=None):
        self.request = request

    def send_notification_email(self, to_email_list,subject, msg_body, urls):
        from_email = settings.FROM_EMAIL

        if to_email_list is not None:
            has_failed=False
            send_record={}
            for to_email in to_email_list:
                try:
                    msg = EmailMessage(
                        subject,
                        msg_body,
                        from_email,
                        to_email,
                    )
                    msg.content_subtype = "html"  # Main content is now text/html
                    msg.send()
                    send_record.update({to_email:1})    # 1 = Success
                except Exception as e:
                    Log.general_log(log_text=str(e))
                    has_failed=True
                    send_record.update({to_email: 0})   # 0 = Failed
                    pass
