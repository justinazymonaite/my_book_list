from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.Book
        fields = ('id', 'book','comment', 'user', 'created_at', 'user_id')