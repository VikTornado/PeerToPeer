from django.shortcuts import render
from news.models import News
from datetime import datetime
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
    page = AboutPage.objects.first()
    return render(request, 'includes/about.html', {'page': page})




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

