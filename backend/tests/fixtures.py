import pytest

from .factories import UserFactory, TodoFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def todo_data():
    return TodoFactory()
