from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()

    creator = models.ForeignKey(User, related_name ="author")
    attending = models.ManyToManyField(User)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'date': self.date,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'creator': self.creator.username,
            # 'attending': self.attending
        } 