from django.shortcuts import render, HttpResponse, redirect
from .sender import SendEmail
from . import forms
from .models import Mails, Topic
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .tasks import send_email, send_beat_email


def home(request):
    return HttpResponse('<h1>HELLO WORLD</h1>')


def subscribe(request):
    if request.method == 'POST':
        form = forms.EmailForm(request.POST)
        all_accounts = Mails.objects.all()
        if request.POST['mail'] not in [account.mail for account in all_accounts]:
            if form.is_valid():
                form.save()
        else:
            messages.success(request, 'Пользователь с данной почтой уже существует')
        return redirect('sub')
    else:
        form = forms.EmailForm()
    return render(request, 'subscription.html', {'form' : form})


def write(request):
    if request.method == 'POST':
        form = forms.TopicCreatiomForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.TopicCreatiomForm()
    return render(request, 'write.html', {'form' : form})


def show_topics(request):
    all_topics = Topic.objects.all()
    all_mails = Mails.objects.all()

    if request.method == 'POST':
        chosen_id = request.POST['chosen_id']
        try:
            chosen_topic = Topic.objects.get(id=chosen_id)
            send_email(
                chosen_topic.subject,
                chosen_topic.content,
                [email.mail for email in all_mails],
            )
        except ObjectDoesNotExist:
            messages.success(request, 'Тема не найдена')
            return redirect('view')

    return render(request, 'view_all.html', {'topics':all_topics, 'mails':all_mails})


def start_spam(request):
    all_mails = Mails.objects.all()
    send_beat_email([email.mail for email in all_mails])
    return redirect('view')