import factory
from factory import fuzzy

from pixida.todo.models import ToDo


class ToDoFactory(factory.django.DjangoModelFactory):
    title = fuzzy.FuzzyText(length=15)
    description = fuzzy.FuzzyText(length=150)

    class Meta:
        model = ToDo
