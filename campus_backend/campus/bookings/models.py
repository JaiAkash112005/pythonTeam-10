from django.db import models


class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
