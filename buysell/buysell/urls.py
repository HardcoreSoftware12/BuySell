
from django.contrib import admin
from django.urls import path
from core.views import index,contact

#to handle or display images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("contact/",contact,name="contact"),
    path('admin/', admin.site.urls),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
