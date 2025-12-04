from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import AboutPage, ProjectsPage, VolunteeringPage, StatutPage, ContactPage, InternationalPage

@admin.register(AboutPage)
class AboutPageAdmin(TranslationAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)

@admin.register(VolunteeringPage)
class VolunteeringPageAdmin(TranslationAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)

@admin.register(ProjectsPage)
class ProjectsPageAdmin(TranslationAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)

@admin.register(StatutPage)
class StatutPageAdmin(TranslationAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)

@admin.register(ContactPage)
class ContactPageAdmin(TranslationAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)

@admin.register(InternationalPage)
class InternationalPageAdmin(TranslationAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
