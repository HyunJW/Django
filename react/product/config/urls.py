from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("list", views.list),
    path("insert", views.insert),
]