from django.db import models

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set, non-editable
    title = models.CharField(max_length=100)  # Mandatory field
    description = models.TextField(max_length=1000)  # Mandatory field
    due_date = models.DateField(null=True, blank=True)  # Optional
    tags = models.ManyToManyField('Tag', blank=True)  # Optional field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')  # Mandatory field

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
