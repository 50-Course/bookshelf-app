from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
from django.db.models import DateField, CharField, TextField, UUIDField, ForeignKey
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# id
# title
# author
# categories - {comic. fantasy, action, thriller, contemporary}
# book cover
# description
# publication date


class Book(models.Model):
    """Instance of book object."""

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    title = CharField(_("Title"), max_length=100, blank=False)
    description = TextField(editable=True, blank=True, null=True, default="")
    author = CharField(max_length=200)
    pub_date = DateField(_("Date Published"), auto_now=True, unique=True, editable=False)

    def __str__(self):
        return self.title or _("Book %s published %s") % self.title, self.pub_date

    def get_absolute_url(self):
        """Inspect absolute Book's object URL."""
        return reverse('book_edit', kwargs={'id': self.id})