import factory
from user_app import models

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: f'user_{n}')
