from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    book = serializers.ReadOnlyField(source='book.id')

    class Meta:
        model = models.Comment
        fields = ('id', 'book','comment', 'user','user_id', 'created_at')


class BookSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    def get_comments_count(self, obj):
        return models.Comment.objects.filter(book=obj).count()

    class Meta:
        model = models.Book
        fields = ('id', 'book','review', 'user', 'created_at', 'user_id','comments_count', 'comments')