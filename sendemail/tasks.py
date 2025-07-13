from celsen.celery import app

from .sender import SendEmail
from .models import Mails, Topic


@app.task
def send_email(subject : str, content : str, user_mails : list) -> None:
    spam_send = SendEmail()
    spam_send.send(
        subject,
        content,
        user_mails,
    )


@app.task
def send_beat_email(mails : list) -> None:
    spam_send = SendEmail()
    spam_send.send(
        subject='Спам от Артюши',
        text="Эта херня генерится каждую минуту",
        email=mails,
    )