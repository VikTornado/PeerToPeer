from django.shortcuts import render, get_object_or_404
from .models import News
from collections import defaultdict

from django.core.paginator import Paginator

def news_list(request):
    all_news = News.objects.all().order_by('-created_at')
    paginator = Paginator(all_news, 9)  # Show 9 news per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/news_archive.html', {
        'page_obj': page_obj,
        'news_list': page_obj  # Keep news_list for compatibility if needed, but page_obj is iterable
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})