from django.contrib import admin
from .models import Tasks

# Register your models here.
@admin.register(Tasks)
class ArticleModal(admin.ModelAdmin):
    list_filter = ('id', 'description', 'status')
    list_display = ('id', 'description', 'status')
# admin.site.register(Person)