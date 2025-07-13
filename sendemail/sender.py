from django.core.mail import send_mail
from django.conf import settings


class SendEmail:
    SENDER_EMAIL = settings.EMAIL_HOST_USER
    
    def send(self, subject : str, text : str, email : list) -> int:
        return send_mail(
            subject = subject,
            message = text,
            from_email = self.SENDER_EMAIL,
            recipient_list = email,
            fail_silently = False,
        )