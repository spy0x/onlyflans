from django.contrib import admin

from .models import ContactForm, Flan, Recipe

admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(Recipe)