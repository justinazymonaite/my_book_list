from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    book = models.CharField(_("book"), max_length=100)
    comment = models.TextField(_("comment"))
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
