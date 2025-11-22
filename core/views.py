from django.shortcuts import render, get_object_or_404
from news.models import News
from datetime import datetime
from collections import defaultdict
from .models import AboutPage, InternationalPage, VolunteeringPage, ProjectsPage
from core.models import StatutPage


def home(request):
    # Отримати 3 останні новини
    news_list = News.objects.order_by('-created_at')[:3]
    return render(request, 'includes/home.html', {'news_list': news_list, 'year': datetime.now().year})


def international_view(request):
    page = InternationalPage.objects.first()
    return render(request, 'includes/international.html', {'page': page})


def volunteering_view(request):
    page = VolunteeringPage.objects.first()
    return render(request, "includes/volunteering.html", {"page": page})


def about_view(request):
    page = get_object_or_404(AboutPage)
    return render(request, 'includes/about.html', {'page': page})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})


def news_list(request):
    news_by_year = defaultdict(list)
    all_news = News.objects.all().order_by('-created_at')
    for item in all_news:
        year = item.created_at.year
        news_by_year[year].append(item)

    sorted_years = sorted(news_by_year.items(), reverse=True)
    return render(request, 'news/news_list.html', {'news_by_year': sorted_years})


def statut_view(request):
    page = StatutPage.objects.first()
    return render(request, 'includes/statut.html', {'page': page})


def projects_page(request):
    page = ProjectsPage.objects.first()
    return render(request, 'includes/projects.html', {'page': page})


def contacts(request):
    return render(request, 'includes/contacts.html')


def contacts_view(request):
    return render(request, 'includes/contacts.html')

