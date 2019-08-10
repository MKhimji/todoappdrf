from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from entries import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('entries/',
        views.EntryList.as_view(),
        name='entries-list'),
    path('entries/<int:pk>/',
        views.EntryDetail.as_view(),
        name='entries-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])

