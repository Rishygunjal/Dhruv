from django.db import models

# Create your models here.


class Hero(models.Model):
    user_id = models.CharField(max_length=60)
    email = models.EmailField()
    is_success = models.BooleanField(default=False)
    roll_number = models.CharField(max_length=60)
    numbers = models.array(models.IntegerField())
    alphabets = models.array(models.CharField())

    def __str__(self):
        return self.name
