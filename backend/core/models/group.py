from django.db import models
from .archetype import Archetype
from .book import Book

class Group(models.Model):
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    group_pic_url = models.URLField(blank=True, null=True)
    group_pic_cloudinary_id = models.CharField(max_length=255, blank=True, null=True)
    current_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='current_in_groups')
    books_read = models.ManyToManyField(Book, blank=True, related_name='read_in_groups')

    def member_count(self):
        return self.members.count()

    def __str__(self):
        return f"{self.archetype.name} Group {self.id}"
    
    def assign_next_book(self):
        read_books = self.books_read.all()
        unread_books = Book.objects.filter(archetype=self.archetype).exclude(id__in=read_books.values_list('id', flat=True))

        if unread_books.exists():
            next_book = unread_books.first()
        else:
            next_book = fetch_new_book(self.archetype)

        self.current_book = next_book
        self.books_read.add(next_book)
        self.save()    