"""
URL configuration for Eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include function added
from django.conf import settings
from django.conf.urls.static import static
from store.views import about_us ,contact_us
from store.views import registration_page ,login_page ,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),  # Include store app URLs
    path('about/', about_us, name='about_us'),
    path('contact/', contact_us, name='contact_us'),
    path('register/', registration_page, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_view, name='logout'),
 
    
]

# Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

