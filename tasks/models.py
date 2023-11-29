from django.db import models
from django.urls import reverse

class CustomUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Task(models.Model):
    owner = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    due_date = models.DateField(null=True)
    is_done = models.BooleanField(default=False)
    
    priority = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.owner}: {self.title} ({self.due_date})"
    
    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk}) 
    