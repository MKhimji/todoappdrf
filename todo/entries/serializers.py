from rest_framework import serializers
from entries.models import Entry
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['date_posted', 'title', 'body', 'author']
