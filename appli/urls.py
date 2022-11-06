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
    path("dashboard/", projects.views.dashboard, name="dashboard"),
    path("create/", projects.views.create, name="create"),
    path("create_category/", projects.views.createCategory, name="create_category"),
    path("create_ticket/", projects.views.createTicket, name="create_ticket"),
    path("projects/", projects.views.index, name="all_projects"),
    path("projects/<str:slug>/", projects.views.index, name="byID_project"),
    path("projects/<str:slug>/edit/", projects.views.editProject, name="edit_project"),
    path("projects/<str:slug>/delete/", projects.views.deleteProject, name="delete_project"),
    path("tickets/", projects.views.indexTickets, name="all_tickets"),
    path("tickets/<str:slug>/", projects.views.indexTickets, name="byID_ticket"),
    path("tickets/<str:slug>/edit/", projects.views.editTicket, name="edit_ticket"),
    path("tickets/<str:slug>/delete/", projects.views.deleteTicket, name="delete_ticket"),
    path("category/", projects.views.indexCategories, name="all_categories"),
    path("category/<str:slug>/", projects.views.indexCategories, name="byID_category"),
    path("category/<str:slug>/edit/", projects.views.editCategory, name="edit_category"),
    path("category/<str:slug>/delete/", projects.views.deleteCategory, name="delete_category"),
    path("profile/", account.views.profile, name="profile"),
    path("profile/edit/", account.views.editProfile, name="edit_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
