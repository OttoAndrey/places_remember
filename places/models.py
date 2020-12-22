from django.contrib.auth.models import User
from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    lng = models.DecimalField(
        max_digits=17,
        decimal_places=15,
    )
    lat = models.DecimalField(
        max_digits=17,
        decimal_places=15,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
