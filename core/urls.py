from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
from .views import (
    home, about_view, projects_page, statut_view,
    international_view, volunteering_view
)
from django.views.i18n import set_language


urlpatterns = [
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('projects/', projects_page, name='projects'),
    path('statut/', statut_view, name='statut'),
    path('international/', international_view, name='international'),
    path('volunteering/', volunteering_view, name='volunteering'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('donate/', views.donate_view, name='donate'),
    path('volunteer-apply/', views.volunteer_apply, name='volunteer_apply'),
    path('publication/<str:type_id>/', views.publication_detail, name='publication_detail'),
    path('set-language/', set_language, name='set_language'),
    # Trigger reload
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)