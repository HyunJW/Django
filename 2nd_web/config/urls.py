from django.contrib import admin
from django.urls import path
from mytest.views import ch01

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ch01.home),
    path('hello/', ch01.hello),
    path('now/', ch01.now),
    path('array/', ch01.array),
]
