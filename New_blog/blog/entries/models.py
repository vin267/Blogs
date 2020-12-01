from django.db import models

from django.contrib.auth.models import User


class Entry(models.Model):
    """
        Creates Model for a post in the database.
    """
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """
            A string representation of the post model.
        """
        return self.entry_title

