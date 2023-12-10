from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        get_user_model(), related_name="todos", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}\n{self.description}"

    def save(self, *args, **kwargs):
        user = kwargs.pop("user", None)

        if not self.owner_id and user:
            self.owner = user

        super().save(*args, **kwargs)

    class Meta:
        app_label = "notes"
