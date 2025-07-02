from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message
from django.contrib import messages

@login_required
def inbox(request):
    recibidos = Message.objects.filter(receiver=request.user).select_related('sender')
    enviados = Message.objects.filter(sender=request.user).select_related('receiver')
    return render(request, 'messenger/inbox.html', {
        'recibidos': recibidos,
        'enviados': enviados
    })

@login_required
def sent_messages(request):
    sent = Message.objects.filter(sender=request.user).order_by('-timestamp').select_related('receiver')
    return render(request, 'messenger/sent.html', {'messages': sent})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/send.html', {'form': form})
