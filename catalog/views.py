from django.shortcuts import render

def index(request):
    return render(request, 'catalog/index.html')

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Польpователь {name} оставил заявку и оставил сообщение:\n{message}\nТелефон для связи: {phone}")
    return render(request, 'catalog/contacts.html')
