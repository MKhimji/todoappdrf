from django.shortcuts import render

# Create your views here.
from entries.models import Entry
from entries.serializers import EntrySerializer
from rest_framework import generics


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
