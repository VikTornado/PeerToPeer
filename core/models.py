from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _



class AboutPage(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = RichTextField("Контент", blank=True)
    updated_at = models.DateTimeField("Оновлено", auto_now=True)

    class Meta:
        verbose_name = "Сторінка 'Про нас'"
        verbose_name_plural = "Сторінка 'Про нас'"

    def __str__(self):
        return self.title

class ContactPage(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контакти"
        verbose_name_plural = "Контакти"

class InternationalPage(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видання та публікації"
        verbose_name_plural = "Видання та публікації"

class ProjectsPage(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Участь у проектах"
        verbose_name_plural = "Участь у проектах"

class VolunteeringPage(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Волонтерство та Освіта"
        verbose_name_plural = "Волонтерство та Освіта"

class StatutPage(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    document = models.FileField(upload_to='documents/', blank=True, null=True, verbose_name=_("Document (PDF)"))
    document_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Document Name"), help_text=_("e.g. Statute of the Organization"))
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Міжнародна діяльність"
        verbose_name_plural = "Міжнародна діяльність"