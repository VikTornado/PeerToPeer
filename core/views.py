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


def donate_view(request):
    return render(request, 'includes/donate.html')


from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@require_POST
def volunteer_apply(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        if not name or not email or not phone:
            return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)

        # Send email
        subject = f'New Volunteer Application: {name}'
        message = f'Name: {name}\nEmail: {email}\nPhone: {phone}'
        from_email = 'noreply@peertopeer.ua'
        recipient_list = ['info@peertopeer.ua']  # Change to actual admin email

        send_mail(subject, message, from_email, recipient_list)

        return JsonResponse({'success': True, 'message': 'Application sent successfully!'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

