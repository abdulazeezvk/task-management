from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# class Task(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     assigned_person = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class TaskLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    log_entry = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.name} - {self.log_entry} - {self.timestamp}"
