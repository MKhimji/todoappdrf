from rest_framework import serializers
from entries.models import Entry
from django.contrib.auth.models import User
class EntrySerializer(serializers.ModelSerializer):
    # Despite foriegnkey on Entry model to User model
    # When you go to /entries/ that gives you the list
    # of entries, but under author, there is just an id
    # need to add perform_create to EntryList in views.py
    # and then add the field below to its serializer.
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Entry
        fields = ['date_posted', 'title', 'body', 'author']


class UserSerializer(serializers.ModelSerializer):
    # forward relationship is from Entry to User
    # reverse from User to Entry
    entries = serializers.PrimaryKeyRelatedField(many=True, queryset=Entry.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'entries']
