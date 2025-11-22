from django.contrib import admin
from .models import AboutPage, ProjectsPage, VolunteeringPage, StatutPage, ContactPage, InternationalPage



@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)



@admin.register(VolunteeringPage)
class VolunteeringPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)


@admin.register(ProjectsPage)
class ProjectsPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)

@admin.register(StatutPage)
class StatutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)


@admin.register(InternationalPage)
class InternationalPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
