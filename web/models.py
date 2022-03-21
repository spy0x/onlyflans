from django.db import models
import uuid

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=None)
    name = models.CharField(max_length=64)
    description = models.TextField(default=None)
    image_url = models.URLField(default=None)
    slug = models.SlugField(default=None)
    is_private = models.BooleanField(default=None)

    def __str__(self):
        return self.name
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField(default=None)
    customer_name = models.CharField(max_length=64)
    message = models.TextField(default=None)
    