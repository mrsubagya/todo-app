from django.db import models

# Create your models here.
class Task(models.Model):
    Priority = (('L', 'Low'),
                ('M', 'Medium'),
                ('H', 'High'))
    
    task_name = models.CharField(max_length=200)
    due_date = models.DateTimeField(default=None, null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=6, choices=Priority, default='L')
    
    def __str__(self):
        return self.task_name 