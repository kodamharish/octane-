from django.db import models

# Create your models here.
class Event(models.Model):
    payload = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

