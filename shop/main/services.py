from django.contrib.auth.hashers import make_password

from .models import User


def create_user(surname, name, email, password, avatar):

    if User.objects.filter(email=email).exists():
        return None

    user = User(
        surname=surname,
        name=name,
        email=email,
        password_hash=make_password(password),
        avatar=avatar
    )

    user.save()

    return user
