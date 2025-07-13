from django.db import models
from django.conf import settings

# Create your models here.
class Topic(models.Model):
    subject = models.CharField(max_length=50, verbose_name="Тема")
    content = models.TextField(verbose_name="Текст сообщения")

    def __str__(self):
        return self.subject

class Mails(models.Model):
    name = models.CharField(verbose_name="Имя")
    mail = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return self.mail