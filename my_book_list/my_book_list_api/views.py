from django.shortcuts import render
from rest_framework import generics, permissions
from . import models, serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        book = models.Book.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if book.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not delete the book review which is not yours.'))

    def put(self, request, *args, **kwargs):
        book = models.Book.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if book.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not change the book review which is not yours.'))

class CommentList(generics.ListCreateAPIView):
    # queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        book = models.Book.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, book=book)

    def get_queryset(self):
        book = models.Book.objects.get(pk=self.kwargs['pk'])
        return models.Comment.objects.filter(book=book)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        comment = models.Comment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not delete the comment which is not yours.'))

    def put(self, request, *args, **kwargs):
        comment = models.Comment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You can not change the comment which is not yours.'))