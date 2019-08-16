from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from entries import views
from entries.views import EntryViewSet, UserViewSet, api_root
from rest_framework import renderers

entries_list = EntryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
entries_detail = EntryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('entries/', entries_list,
        name='entries-list'),
    path('entries/<int:pk>/', entries_detail,
        name='entries-detail'),
    path('users/',user_list,
        name='user-list'),
    path('users/<int:pk>/', user_detail,
        name='user-detail')
])




