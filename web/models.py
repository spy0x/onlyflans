from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=None)
    name = models.CharField(max_length=64)
    description = models.TextField(default=None)
    image_url = models.URLField(default=None)
    slug = models.SlugField(default=None)
    is_private = models.BooleanField(default=None)

    def __str__(self):
        return self.name