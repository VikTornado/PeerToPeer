import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peertopeer.settings')
django.setup()

from news.models import News, NewsImage

def populate_news():
    news_data = [
        {
            'title': 'Запуск нового волонтерського хабу',
            'content': '<p>Ми раді оголосити про відкриття нового координаційного центру для волонтерів. Це дозволить нам швидше реагувати на запити про допомогу.</p>',
            'image_path': 'news/1763809278-4304-large.webp'
        },
        {
            'title': 'Гуманітарна місія до деокупованих регіонів',
            'content': '<p>Наша команда доставила понад 5 тонн продуктів харчування та засобів гігієни мешканцям прифронтових територій.</p>',
            'image_path': 'news/69204a34b19a58.75262119.jpg'
        },
        {
            'title': 'Зустріч з міжнародними партнерами',
            'content': '<p>Обговорили стратегію співпраці на 2026 рік. Партнери підтвердили готовність підтримувати наші освітні проекти.</p>',
            'image_path': 'news/Kerivnyk-2-scaled.jpg'
        }
    ]

    for data in news_data:
        news, created = News.objects.get_or_create(
            title=data['title'],
            defaults={'content': data['content']}
        )
        if created:
            if os.path.exists(os.path.join('media', data['image_path'])):
                news.main_image = data['image_path']
                news.save()
            print(f"News created: {data['title']}")
        else:
            print(f"News already exists: {data['title']}")

if __name__ == '__main__':
    populate_news()
