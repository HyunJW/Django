from django.contrib import admin
from django.urls import path, include, re_path
from config import views
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home),
    path('address/', include('address.urls')),
    path('memo/', include('memo.urls')),
    path('book/', include('book.urls')),
    path('transaction/', include('transaction.urls')),
    path('procedure/', include('procedure.urls')),
    path('mymember/', include('mymember.urls')),
    path('ajax/', include('ajax.urls')),
    path('survey/', include('survey.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]