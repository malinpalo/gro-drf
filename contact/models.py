from django.db import models


class Contact(models.Model):
    """
    Model for the contact.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.last_name}'