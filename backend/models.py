from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# Create your models here.

class Port(models.Model):
    port = models.PositiveIntegerField(
        validators=(
            MaxValueValidator(65535),
            MinValueValidator(1)
        ),
        unique=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.port} @ {self.owner}'


class Flow(models.Model):
    port = models.ForeignKey(
        Port,
        on_delete=models.PROTECT
    )
    datetime = models.DateTimeField(auto_now_add=True)
    flow = models.PositiveIntegerField()

    def __str__(self):
        flow = self.flow
        unit = 'B'
        if flow >= 1024:
            flow /= 1024
            unit = 'KB'
            if flow >= 1024:
                flow /= 1024
                unit = 'MB'
                if flow >= 1024:
                    flow /= 1024
                    unit = 'GB'

        return f'{self.port} @ {self.datetime.timetz()} : {flow:.2f} {unit}'
