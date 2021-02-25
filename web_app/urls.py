"""web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from about import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('Sit1babIedm-Ilh2d/', admin.site.urls),                # Admin page Sit1babIedm-Ilh2d
    path('', include('users.urls')),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('about_/', views.about_view_v2, name='about_v2'),
    path('pricing/', views.pricing_view, name='pricing_index'),
    path('pricing_/', views.pricing_view_v2, name='pricing_index_v2'),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('finfolio/', include('finfolio.urls')),
    path('', include('companies.urls')),
    path('privacy-notice/', views.privacy_view, name='privacy'),
    path('terms-and-conditions/', views.terms_view, name='terms'),
    path('djga/', include('google_analytics.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
