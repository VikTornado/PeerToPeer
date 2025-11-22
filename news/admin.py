from django.contrib import admin
from .models import News, NewsImage
from core.models import InternationalPage, ContactPage
from django.contrib.admin.sites import AlreadyRegistered


class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'external_url')
    inlines = [NewsImageInline]


try:
    admin.site.register(News, NewsAdmin)
except AlreadyRegistered:
    pass


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)


@admin.register(InternationalPage)
class InternationalPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)