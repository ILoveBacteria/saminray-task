from django.db import models


class NameServer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.name
