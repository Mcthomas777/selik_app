from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "re_agent_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("property/add/", views.add_estate, name="add_estate"),
    path("contact/add/", views.add_contact, name="add_contact"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
