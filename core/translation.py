from modeltranslation.translator import register, TranslationOptions
from .models import InternationalPage, VolunteeringPage, ProjectsPage, AboutPage, StatutPage, ContactPage

@register(InternationalPage)
class InternationalPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(VolunteeringPage)
class VolunteeringPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(ProjectsPage)
class ProjectsPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(AboutPage)
class AboutPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(StatutPage)
class StatutPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'document_name')

@register(ContactPage)
class ContactPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
