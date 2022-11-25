from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    book = models.CharField(_("book"), max_length=100)
    review = models.TextField(_("review"), max_length=10000)
    user = models.ForeignKey(
        User, verbose_name=_("user"), 
        on_delete=models.CASCADE, 
        related_name="books",
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self) -> str:
        return _("{book} listed by {user} at {created_at}").format(
            book=self.book,
            user=self.user,
            created_at=self.created_at,
        )

    class Meta:
        ordering = ('-created_at', )


class Comment(models.Model):
    book = models.ForeignKey(Book, verbose_name=_('book'), on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(_("comment"), max_length=10000)
    user = models.ForeignKey(
        User, verbose_name=_("user"), 
        on_delete=models.CASCADE, 
        related_name="comments",
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self) -> str:
        return _("Comment on {book_id} by {user} at {created_at}").format(
            book_id=self.book.id,
            user=self.user,
            created_at=self.created_at,
        )
