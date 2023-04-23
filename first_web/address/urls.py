from address import views
from django.urls import path

# url mapping
urlpatterns = [
    path('', views.home),
    path('write', views.write),
    path('insert', views.insert),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
]