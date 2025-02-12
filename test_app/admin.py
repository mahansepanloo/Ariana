from django.contrib import admin
from test_app.models import Article, Knowledge


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')
