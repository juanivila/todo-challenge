import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        username="testuser", password="testpassword"
    )


@pytest.fixture
def todo_data():
    return {
        "title": "Test Todo",
        "description": "This is a test todo.",
    }
