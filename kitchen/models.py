from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=69, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name