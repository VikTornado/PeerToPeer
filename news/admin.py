from django.contrib import admin
from .models import News, NewsImage


class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'external_link')
    inlines = [NewsImageInline]


admin.site.register(News, NewsAdmin)