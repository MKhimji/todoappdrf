from rest_framework import serializers

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['date_posted', 'title', 'body', 'author']
