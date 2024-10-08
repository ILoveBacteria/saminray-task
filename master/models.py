from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name
