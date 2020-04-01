from django.contrib import admin
from bookshop.models import Author, Book, Genre, Comment, Buyer

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Buyer)

# Register your models here.
