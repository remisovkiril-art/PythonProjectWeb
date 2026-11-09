from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def news(request):
    context = {
        'title': 'Новини міста',
        'text': 'Тут можна дізнатися про події, новини та важливу інформацію міста Дніпро.',
        'items': [
            'Міські події та заходи',
            'Транспорт та інфраструктура',
            'Освіта та культура',
            'Спорт та громадське життя'
        ]
    }

    return render(request, 'main/section.html', context)


def management(request):
    context = {
        'title': 'Керівництво міста',
        'text': 'Міське управління Дніпра здійснюється міською радою та її виконавчими органами.',
        'items': [
            'Міський голова — Борис Філатов',
            'Міська рада',
            'Виконавчий комітет міської ради',
            'Департаменти та управління міської ради'
        ]
    }

    return render(request, 'main/section.html', context)


def facts(request):
    context = {
        'title': 'Факти про місто',
        'text': 'Дніпро — велике місто України, розташоване на берегах річки Дніпро.',
        'items': [
            'Місто розташоване на річці Дніпро.',
            'Дніпро є важливим промисловим та науковим центром України.',
            'У місті знаходиться один із найдовших міських набережних просторів Європи.',
            'Місто має розвинену транспортну та залізничну інфраструктуру.',
            'Однією з відомих пам’яток є Монастирський острів.'
        ]
    }

    return render(request, 'main/section.html', context)


def contacts(request):
    context = {
        'title': 'Контактні телефони міських служб',
        'text': 'Номери телефонів для звернення до екстрених та міських служб.',
        'items': [
            '112 — єдиний номер екстреної допомоги',
            '101 — пожежно-рятувальна служба',
            '102 — поліція',
            '103 — швидка медична допомога',
            '104 — аварійна газова служба',
            '000 000 00 00 — міська служба оперативного реагування'
        ]
    }

    return render(request, 'main/section.html', context)


def history(request):
    return render(request, 'main/history.html')


def history_people(request):
    return render(request, 'main/history_people.html')

