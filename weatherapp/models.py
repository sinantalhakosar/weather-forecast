from django.db import models
import uuid
# Create your models here.

class City(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, default="Ghost")
    value = models.CharField(max_length=2, default="00")
    latitude = models.CharField(max_length=30, default="0")
    longitude = models.CharField(max_length=30, default="0")