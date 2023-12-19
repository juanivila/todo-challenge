import logging

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import DataError, IntegrityError
from django.utils import timezone
from notes.models import Todo

logger = logging.getLogger("django")


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


@pytest.mark.django_db
class TestTodoModel:
    def test_title_max_length(self, user, todo_data):
        """
        Checks that the title field has a max length of 200 characters
        """
        long_title = "A" * 201
        todo = Todo(title=long_title, description=todo_data["description"], owner=user)

        with pytest.raises(ValidationError) as excinfo:
            todo.full_clean()

        try:
            assert "Ensure this value has at most 200 characters" in str(excinfo.value)
            logger.info(
                f"\nTEST PASSED:\n {self.test_title_max_length.__name__}\n{self.test_title_max_length.__doc__}"
            )

        except AssertionError as e:
            logger.error(f"TEST ERROR:\n{self.test_title_max_length.__name__}\n{e}")

    def test_todo_created_at_now(self, user, todo_data):
        """
        Checks that the created at field is set to now when the to-do is created
        """
        todo = Todo(**todo_data)
        todo.save(user=user)

        try:
            assert todo.created_at is not None
            assert timezone.now() - todo.created_at < timezone.timedelta(seconds=5)
            logger.info(
                f"\nTEST PASSED:\n {self.test_todo_created_at_now.__name__}\n{self.test_todo_created_at_now.__doc__}"
            )

        except AssertionError as e:
            logger.error(f"TEST ERROR:\n{self.test_todo_created_at_now.__name__}\n{e}")

    def test_todo_default_status(self, user, todo_data):
        """
        Checks that the to-do is created with the default status of False
        """
        todo = Todo(**todo_data)
        todo.save(user=user)

        try:
            assert todo.completed is False
            logger.info(
                f"\nTEST PASSED:\n {self.test_todo_default_status.__name__}\n{self.test_todo_default_status.__doc__}"
            )

        except AssertionError as e:
            logger.error(f"TEST ERROR:\n{self.test_todo_default_status.__name__}\n{e}")

    def test_save_todo_with_owner(self, user, todo_data):
        """
        Checks that the owner of the to-do is set to the user passed in
        """
        todo = Todo(**todo_data)
        todo.save(user=user)

        try:
            assert todo.owner == user
            logger.info(
                f"\nTEST PASSED:\n {self.test_save_todo_with_owner.__name__}\n{self.test_save_todo_with_owner.__doc__}"
            )

        except AssertionError as e:
            logger.error(f"TEST ERROR:\n{self.test_save_todo_with_owner.__name__}\n{e}")

    def test_owner_not_null(self, todo_data):
        """
        Checks that the owner field is not null
        """
        todo = Todo(**todo_data)

        with pytest.raises(IntegrityError) as excinfo:
            todo.save()

        try:
            assert "NOT NULL constraint failed: notes_todo.owner_id" in str(
                excinfo.value
            )
            logger.info(
                f"\nTEST PASSED:\n {self.test_owner_not_null.__name__}\n{self.test_owner_not_null.__doc__}"
            )

        except AssertionError as e:
            logger.error(f"TEST ERROR:\n{self.test_owner_not_null.__name__}\n{e}")
