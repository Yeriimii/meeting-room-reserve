"""
URL configuration for myreserve project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings  # media file
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path("", RedirectView.as_view(
        pattern_name='reserveapp:reservedroom_list',
    ), name='root'),
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("reserveapp/", include('reserveapp.urls')),
]

if settings.DEBUG:  # static 파일과 다르게, 장고 개발서버에서 서빙 미지원. 개발 편의성 목적으로 직접 서빙 Rule 추가 가능
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include("debug_toolbar.urls"))
    ]