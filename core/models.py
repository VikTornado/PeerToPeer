from django.db import models
from ckeditor.fields import RichTextField


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

class InternationalPage(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProjectsPage(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class VolunteeringPage(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class StatutPage(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title