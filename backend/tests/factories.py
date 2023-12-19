import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall("set_password", "testpassword")


class TodoFactory(factory.Factory):
    class Meta:
        model = dict  # Since it's just a dictionary, not a Django model

    title = factory.Faker("sentence", nb_words=15)
    description = factory.Faker("paragraph")
