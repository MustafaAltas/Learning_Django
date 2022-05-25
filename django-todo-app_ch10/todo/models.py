from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    PRIORITY  = {
        ("1", "Hight"),
        ("2", "Medium"),
        ("3", "Low"),
    }
    priority = models.CharField(max_length=10,choices=PRIORITY)
    isCompleted = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"
    

# Create your models here.
