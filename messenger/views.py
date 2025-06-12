from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required

@login_required
def inbox(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'messenger/inbox.html', {'mensajes': mensajes})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'messenger/send_message.html', {'form': form})