"""appli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import account.views
import intranet.views
import projects.views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", intranet.views.index, name="index"),
    path("register/", account.views.register, name="register"),
    path("login/", account.views.login, name="login"),
    path("logout/", account.views.logout, name="logout"),
    path("create/", projects.views.create, name="create"),
    path("create_category/", projects.views.createCategory, name="create_category"),
    #path("project/<int:project_id>/", projects.views.project, name="project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
