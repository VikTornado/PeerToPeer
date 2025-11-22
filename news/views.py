from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news_queryset = News.objects.order_by('-created_at')
    paginator = Paginator(news_queryset, 6)  # 6 новин на сторінку

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/news_list.html', {'page_obj': page_obj})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})