from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


#http://127.0.0.1:8000

from django.shortcuts import render


def home(request):
    cards = [
        {
            'title': 'Django',
            'text': 'Django is a popular Python web framework',
            'image': 'main/images/django1.png'
        },
        {
            'title': 'Python',
            'text': 'Python is being used for creating websites',
            'image': 'main/images/django2.png'
        },
        {
            'title': 'Web Development',
            'text': 'Creation of current websites using Django',
            'image': 'main/images/django3.png'
        }
    ]

    return render(request, 'main/index.html', {'cards': cards})


def about(request):
    text = 'Це сторінка про Нас'

    frameworks = ['Django', 'Flask', 'Python']

    return render(request, 'main/about.html', context={
        'text': text,
        'frameworks': frameworks
    })

