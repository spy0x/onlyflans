from django.db import models
from django.forms import ModelForm
import uuid
from .forms import DateInput

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=None)
    name = models.CharField(max_length=64)
    description = models.TextField(default=None)
    image_url = models.URLField(default=None)
    slug = models.SlugField(default=None)
    is_private = models.BooleanField(default=None)

    def __str__(self):
        return self.name
        
class Recipe(models.Model):
    receta_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField(default=None)
    image_url = models.URLField(default=None)
    page_url = models.URLField(default=None)

    def __str__(self):
        return self.title

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField(default=None)
    customer_name = models.CharField(max_length=64)
    customer_birthday = models.DateField()
    message = models.TextField(default=None)

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name','customer_birthday', 'message']
        widgets = {
            "customer_birthday": DateInput()
        }