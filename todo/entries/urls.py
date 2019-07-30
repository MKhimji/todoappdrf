from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('entries/', views.EntryList.as_view()),
    path('entries/<int:pk>/', views.EntryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
