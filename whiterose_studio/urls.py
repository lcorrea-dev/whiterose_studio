"""whiterose_studio URL Configuration

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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('admin/', admin.site.urls),
    path('', include('apps.blog.urls'), name='home'),
    path('user/', include('apps.user.urls'), name='user'),

    path('gallery/', include('apps.gallery.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                                template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
