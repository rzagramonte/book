from django.contrib import admin

from .models import Archetype, Book, Group, Message, UserProfile

# Register your models here.
admin.site.register(Book)
admin.site.register(Group)
admin.site.register(Archetype)
admin.site.register(Message)
admin.site.register(UserProfile)
