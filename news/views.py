from django.shortcuts import render, get_object_or_404
from .models import News
from collections import defaultdict

def news_list(request):
    news_by_year = defaultdict(list)
    all_news = News.objects.all().order_by('-created_at')
    for item in all_news:
        year = item.created_at.year
        news_by_year[year].append(item)

    sorted_years = sorted(news_by_year.items(), reverse=True)
    return render(request, 'news/news_list.html', {'news_by_year': sorted_years})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})