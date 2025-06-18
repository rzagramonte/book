from django.contrib import admin
from .models import Book, ChatRoom, ColorType, Message, UserProfile

# Register your models here.
admin.site.register(Book)
admin.site.register(ChatRoom)
admin.site.register(ColorType)
admin.site.register(Message)
admin.site.register(UserProfile)
