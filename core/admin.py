from django.contrib import admin
from news.models import News, NewsImage
from .models import AboutPage, ProjectsPage, VolunteeringPage

class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    inlines = [NewsImageInline]


admin.site.register(News, NewsAdmin)


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

