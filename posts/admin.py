from django.contrib import admin
from .models import Category, Post, Author, AboutPage, Tag, Car

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(AboutPage)
admin.site.register(Car)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin) :
    list_display = ('id' , 'name' , 'created_at')
