from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .cards import cards
import json


def home(request):
    return render(request, 'main/index.html', {'cards': cards})


def get_card(request, id):

    title = None

    if request.GET.get('title'):
        title = request.GET.get('title')

    if id > 0 and id <= len(cards):
        return render(request, 'main/card.html', {
            'card': cards[id - 1],
            'title': title if title else f'Card {id}'
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
        data = json.loads(request.body)

        title = data.get('title')
        description = data.get('description')
        image = data.get('image')

    return JsonResponse({'message': 'ok'})


def register(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        print('Дані реєстрації:')
        print(data)

        return JsonResponse({'message': 'Реєстрація успішна'})

    return render(request, 'main/register.html')



# from django.shortcuts import render
#
#
# def home(request):
#     projects = [
#         {
#             'title': 'OpenAI',
#             'description': 'Соосновал компанию OpenAI, которая занимается исследованиями и разработкой искусственного интеллекта.',
#             'technologies': 'Python, Machine Learning, AI',
#             'result': 'Создание одной из ведущих компаний в сфере искусственного интеллекта.'
#         },
#         {
#             'title': 'Stripe',
#             'description': 'Работал техническим директором Stripe и участвовал в развитии инженерной команды компании.',
#             'technologies': 'Ruby, Python, Software Engineering',
#             'result': 'Помог увеличить команду компании с 4 до 250 сотрудников.'
#         },
#         {
#             'title': 'OpenAI Five',
#             'description': 'Проект искусственного интеллекта, обученного играть в Dota 2 против профессиональных команд.',
#             'technologies': 'Machine Learning, Reinforcement Learning',
#             'result': 'Система искусственного интеллекта смогла соревноваться с профессиональными игроками.'
#         }
#     ]
#
#     context = {
#         'projects': projects
#     }
#
#     return render(request, 'main/index.html', context)