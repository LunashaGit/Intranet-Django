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
    path("create_ticket/", projects.views.createTicket, name="create_ticket"),
    path("projects/", projects.views.index, name="all_projects"),
    path("projects/<str:slug>/", projects.views.byID_project, name="byID_project"),
    path("projects/<str:slug>/edit/", projects.views.editProject, name="edit_project"),
    path("projects/<str:slug>/delete/", projects.views.deleteProject, name="delete_project"),
    # path("ticket/", products.views.tickets, name="all_tickets"),
    # path("ticket/<int:ticket_id>/", products.views.ticket, name="byID_ticket"),
    # path("ticket/<int:ticket_id>/edit/", products.views.editTicket, name="edit_ticket"),
    # path("ticket/<int:ticket_id>/delete/", products.views.deleteTicket, name="delete_ticket"),
    # path("category/", products.views.categories, name="all_categories"),
    # path("category/<int:category_id>/", products.views.category, name="byID_category"),
    # path("category/<int:category_id>/edit/", products.views.editCategory, name="edit_category"),
    # path("category/<int:category_id>/delete/", products.views.deleteCategory, name="delete_category"),
    # path("profile/", account.views.profile, name="profile"),
    # path("profile/edit/", account.views.editProfile, name="edit_profile"),
    #path("project/<int:project_id>/", products.views.project, name="project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
