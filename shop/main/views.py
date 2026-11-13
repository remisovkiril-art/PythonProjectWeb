import datetime as dt
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Card, User
from .cards import cards
from . import services


def home(request):
    return render(request, 'main/index.html', {'cards': cards})


def get_card(request, id):
    title = None

    if request.GET.get('title'):
        title = request.GET.get('title')

    if id > 0 and id <= len(cards):
        return render(request, 'main/card.html', {
            'card': cards[id - 1],
            'title': f'{title if title else "Card " + str(id)}'
        })
    else:
        return HttpResponse("Not Found")


def get_card_by_title(request):
    title = None

    if request.method == 'GET' and request.GET.get('title'):
        title = request.GET.get('title')

    elif request.method == 'POST':
        title = request.POST.get('title')

    if title is not None:
        return JsonResponse({'title': title})
    else:
        return HttpResponse("Not Found")


def about(request):
    text = 'Це сторінка про Нас. Це точно ця сторінка'
    frameworks = []

    return render(request, 'main/about.html', {
        'text': text,
        'frameworks': frameworks,
        'cards': cards,
        'data': [1, 2, 105, 102, 7, 10, 100]
    })


def create_card(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        card = Card(
            title=title,
            description=description,
            image=image,
            created_at=dt.datetime.now()
        )

        card.save()

    return JsonResponse({'message': 'ok'})


def register(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        avatar = request.FILES.get('avatar')

        if not surname or not name or not email or not password:
            return JsonResponse({
                'message': 'Заповніть обов’язкові поля'
            }, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({
                'message': 'Користувач з таким email вже існує'
            }, status=400)

        user = services.create_user(
            surname,
            name,
            email,
            password,
            avatar
        )

        if user is None:
            return JsonResponse({
                'message': 'Користувач з таким email вже існує'
            }, status=400)

        print(user.email)

        return JsonResponse({
            'message': 'Користувача успішно створено'
        })

    return render(request, 'main/register.html')
