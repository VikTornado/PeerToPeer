from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    external_link = models.URLField(blank=True, null=True, help_text="Посилання на зовнішню новину")
    created_at = models.DateTimeField(auto_now_add=True)
    # Основне зображення (для обкладинки)
    main_image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news/gallery/')

    def __str__(self):
        return f"Image for: {self.news.title}"