from django import forms
from .models import Mails, Topic


class EmailForm(forms.ModelForm):
    name = forms.CharField(required=True, help_text='Введите имя')
    mail = forms.EmailField(required=True, help_text='Введите почту')

    class Meta:
        model = Mails
        fields = ['name', 'mail']


class TopicCreatiomForm(forms.ModelForm):
    subject = forms.CharField(label='Введите тему', required=True)
    content = forms.CharField(label='Введите текст', widget=forms.Textarea(
        attrs={
            'rows': 5,
            'cols': 40,
            'style': 'resize: none; width: 100%;',}
        ))
    class Meta:
        model = Topic
        fields = ['subject', 'content']