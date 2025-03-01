from django.shortcuts import render, redirect
from .models import Project, ContactMessage

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return redirect('home')



# to access the messages through contact froms
# def view_messages(request):
#     messages=ContactMessage.objects.all().order_by(-created_at)
#     return render(request,'portfolio/messages.html',{'messages':messages})