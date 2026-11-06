from django.shortcuts import render
from .cards import cards


def home(request):
    return render(request, 'main/index.html', {
        'cards': cards
    })


def get_card(request, id):
    if id > 0 and id <= len(cards):
        return render(request, 'main/card.html', {
            'card': cards[id - 1],
            'title': f'Card {id}'
        })

    return render(request, 'main/not_found.html')


def search_card(request):
    search_title = request.GET.get('title', '').strip()

    for card in cards:
        if card['title'].lower() == search_title.lower():
            return render(request, 'main/card.html', {
                'card': card,
                'title': card['title']
            })

    return render(request, 'main/not_found.html')


def about(request):
    text = 'Це сторінка про Нас. Це точно ця сторінка'
    frameworks = []

    return render(request, 'main/about.html', {
        'text': text,
        'frameworks': frameworks
    })






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