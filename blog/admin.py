from django.contrib import admin
from .models import Article, Category, Tag, Author, Comment, About, Clients
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    filter_horizontal = ('tag',)
    search_fields = ('category',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(About)
admin.site.register(Clients)
