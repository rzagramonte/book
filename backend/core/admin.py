from django.contrib import admin
from .models import Book, Group, Archetype, Message, UserProfile

# Register your models here.
admin.site.register(Book)
admin.site.register(Group)
admin.site.register(Archetype)
admin.site.register(Message)
admin.site.register(UserProfile)
