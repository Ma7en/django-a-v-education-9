from django.db import models


# Create your models here.
class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
